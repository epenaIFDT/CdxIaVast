import yaml
from intents import detect_intent

TEMPLATE_PATH = "prompt_templates.yml"

def load_templates(path=TEMPLATE_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_prompt_with_template(user_input: str, knowledge: dict, templates: dict) -> str:
    categoria = detect_intent(user_input).lower()
    template = templates.get(categoria, {}).get("template")
    if not template:
        return user_input
    # Extraer datos relevantes del knowledge
    context = knowledge.get("mission_vision", {}).get("mission", "")
    catalog = ", ".join(knowledge.get("products_services", {}).get("computo", []))
    faq = ", ".join([q["question"] for q in knowledge.get("frequently_asked_questions", [])])
    history = ", ".join([h["event"] for h in knowledge.get("corporate_history", [])])
    certifications = ", ".join(knowledge.get("certifications", []))
    return template.format(
        question=user_input,
        context=context,
        catalog=catalog,
        faq=faq,
        history=history,
        certifications=certifications
    )
