import sys
from chat import cargar_conocimiento
from intents import detect_intent
from claude_client import ClaudeClient
from utils import sanitize_input
from utils_prompt import load_templates, build_prompt_with_template

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: issue_bot.py <title> <body>")
        sys.exit(1)
    title = sys.argv[1]
    body = sys.argv[2]
    knowledge = cargar_conocimiento()
    templates = load_templates() if knowledge else None
    pregunta = sanitize_input(title + "\n" + body)
    categoria = detect_intent(pregunta)
    if templates:
        prompt = build_prompt_with_template(pregunta, knowledge, templates)
    else:
        prompt = pregunta
    try:
        claude = ClaudeClient()
        respuesta = claude.send_message(prompt)
        print(f"Respuesta automática: {respuesta}")
    except Exception as e:
        print(f"Error al consultar Claude: {e}")
