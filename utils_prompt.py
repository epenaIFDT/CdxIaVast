import yaml
from intents import detect_intent

TEMPLATE_PATH = "prompt_templates.yml"

def load_templates(path=TEMPLATE_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_prompt_with_template(user_input: str, knowledge, templates: dict) -> str:
    categoria = detect_intent(user_input).lower()
    template = templates.get(categoria, {}).get("template")
    if not template:
        return user_input
    # Permitir dict o modelo pydantic
    def get_attr(obj, attr, default=None):
        if isinstance(obj, dict):
            return obj.get(attr, default)
        return getattr(obj, attr, default)

    context = get_attr(get_attr(knowledge, "mission_vision", {}), "mission", "")
    catalog = ", ".join(get_attr(get_attr(knowledge, "products_services", {}), "computo", []))
    # Soportar dict y pydantic para FAQs y corporate_history
    faq_items = get_attr(knowledge, "frequently_asked_questions", [])
    if faq_items and hasattr(faq_items[0], "question"):
        faq = ", ".join([q.question for q in faq_items])
    else:
        faq = ", ".join([q["question"] for q in faq_items])

    history_items = get_attr(knowledge, "corporate_history", [])
    if history_items and hasattr(history_items[0], "event"):
        history = ", ".join([h.event for h in history_items])
    else:
        history = ", ".join([h["event"] for h in history_items])
    certifications = ", ".join(get_attr(knowledge, "certifications", []))
    return template.format(
        question=user_input,
        context=context,
        catalog=catalog,
        faq=faq,
        history=history,
        certifications=certifications
    )
