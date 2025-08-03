from .utils import sanitize_input
import os
import uuid
from .utils_prompt import load_templates, build_prompt_with_template
"""
CLI principal para Chatbot Vastec
"""

# Permite importación de funciones para tests

import sys
from rich.console import Console
from rich.prompt import Prompt
from datetime import datetime
from .context_loader import load_knowledge, VastecKnowledge
from .claude_client import ClaudeClient
from .intents import detect_intent
import os
def get_log_path():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d")
    return os.path.join(log_dir, f"chat_{fecha}.log")

def log_interaction(session_id: str, fecha: datetime, pregunta: str, categoria: str, respuesta: str, error: str = None):
    log_path = get_log_path()
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[SID:{session_id}] [{fecha.strftime('%H:%M:%S')}] [{categoria}] Q: {pregunta}\nA: {respuesta}\n")
        if error:
            f.write(f"[ERROR] {error}\n")
        f.write("\n")

console = Console()

KNOWLEDGE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "vastec_knowledge.json")

def cargar_conocimiento():
    try:
        knowledge = load_knowledge(KNOWLEDGE_PATH)
        console.print("[green]Base de conocimiento cargada correctamente.[/green]")
        return knowledge
    except Exception as e:
        console.print(f"[red]Error al cargar conocimiento:[/red] {e}")
        return None


def build_prompt(user_input: str, knowledge: VastecKnowledge) -> str:
    # Prompt simple, puede mejorarse con plantillas
    return (
        f"Empresa: {knowledge.empresa}\n"
        f"Productos: {[p.nombre for p in knowledge.productos]}\n"
        f"FAQ: {[f.pregunta for f in knowledge.faq]}\n"
        f"Institucional: Misión: {knowledge.institucional.mision}, Certificaciones: {knowledge.institucional.certificaciones}\n"
        f"Pregunta: {user_input}"
    )

def main():
    session_id = str(uuid.uuid4())[:8]
    console.print(f"[bold green]Chatbot Vastec CLI[/bold green] [SID:{session_id}]", style="bold")
    console.print("Escribe tu consulta o usa /reload, /exit, /help", style="cyan")
    history = []
    knowledge = cargar_conocimiento()
    templates = None
    template_path = os.path.join(os.path.dirname(__file__), "..", "data", "prompt_templates.yml")
    if os.path.exists(template_path):
        try:
            templates = load_templates(template_path)
            console.print("[green]Plantillas de prompt cargadas.[/green]")
        except Exception as e:
            console.print(f"[yellow]No se pudieron cargar plantillas: {e}[/yellow]")
    try:
        claude = ClaudeClient()
    except Exception as e:
        console.print(f"[red]Error de API Claude:[/red] {e}")
        claude = None
    while True:
        try:
            user_input = Prompt.ask("[bold blue]Tú[/bold blue]")
        except (KeyboardInterrupt, EOFError):
            console.print("\n[red]Sesión finalizada.[/red]")
            break
        if not user_input.strip():
            continue
        history.append((datetime.now(), user_input))
        if user_input.strip().lower() == "/exit":
            console.print("[yellow]¡Hasta luego![/yellow]")
            break
        elif user_input.strip().lower() == "/reload":
            console.print("[magenta]Recargando base de conocimiento...[/magenta]")
            knowledge = cargar_conocimiento()
            continue
        elif user_input.strip().lower() == "/help":
            console.print("[cyan]Comandos: texto libre, /reload, /exit, /help[/cyan]")
            continue
        else:
            if not knowledge or not claude:
                console.print("[red]No se puede responder: error de conocimiento o API.[/red]")
                log_interaction(session_id, datetime.now(), user_input, "Error", "", error="Sin conocimiento o API")
                continue
            categoria = detect_intent(user_input)
            console.print(f"[blue]Categoría detectada:[/blue] [bold]{categoria}[/bold]")
            pregunta_saneada = sanitize_input(user_input)
            from .utils_search import buscar_info_rapida
            respuesta_directa = buscar_info_rapida(knowledge, pregunta_saneada)
            if respuesta_directa:
                console.print(f"[bold]Respuesta:[/bold] [italic]{respuesta_directa}[/italic]", style="green")
                log_interaction(session_id, datetime.now(), pregunta_saneada, categoria, respuesta_directa)
                continue
            if templates:
                prompt = build_prompt_with_template(pregunta_saneada, knowledge, templates)
            else:
                prompt = build_prompt(pregunta_saneada, knowledge)
            try:
                respuesta = claude.send_message(prompt)
                console.print(f"[bold]Respuesta:[/bold] [italic]{respuesta}[/italic]", style="green")
                log_interaction(session_id, datetime.now(), pregunta_saneada, categoria, respuesta)
            except Exception as e:
                console.print(f"[red]Error al consultar Claude:[/red] {e}")
                log_interaction(session_id, datetime.now(), pregunta_saneada, categoria, "", error=str(e))

if __name__ == "__main__":
    main()
