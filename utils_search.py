"""
Funciones utilitarias para búsqueda directa en la base de conocimiento Vastec.
"""

def buscar_info_rapida(knowledge, pregunta: str) -> str:
    # Liderazgo: gerente general y ejecutivos
    if (
        "gerente" in pregunta or "general" in pregunta or "director" in pregunta or "jefe" in pregunta or "ejecutivo" in pregunta or "lider" in pregunta or "líder" in pregunta or "manager" in pregunta or "administrador" in pregunta
    ):
        ld = getattr(knowledge, "leadership", None)
        partes = []
        if ld:
            if hasattr(ld, "current_general_manager") and ld.current_general_manager:
                partes.append(f"Gerente general: {ld.current_general_manager}")
            if hasattr(ld, "other_key_executives") and ld.other_key_executives:
                otros = [f"{e.name} ({e.position})" for e in ld.other_key_executives if hasattr(e, "name") and hasattr(e, "position")]
                if otros:
                    partes.append(f"Otros ejecutivos: {', '.join(otros)}")
        if partes:
            return " | ".join(partes)
    import unicodedata
    def normaliza(texto):
        texto = texto.lower()
        texto = unicodedata.normalize('NFKD', texto)
        texto = ''.join([c for c in texto if not unicodedata.combining(c)])
        return texto.replace('¿','').replace('?','').replace(',','').replace('.','')

    respuestas = []

    # Encabezados para cada tipo de respuesta
    def encabezado(tipo, contenido):
        return f"[{tipo}]\n{contenido}"

    # Preguntas frecuentes
    faqs = getattr(knowledge, "frequently_asked_questions", [])
    if faqs and hasattr(faqs[0], "question"):
        pregunta_norm = normaliza(pregunta)
        for faq in faqs:
            qtext = normaliza(faq.question)
            palabras_faq = set(qtext.split())
            palabras_user = set(pregunta_norm.split())
            if palabras_faq and len(palabras_user & palabras_faq) / len(palabras_faq) >= 0.5:
                respuestas.append(encabezado("FAQ", f"{faq.question}\n{faq.answer}"))

    # Ubicación
    if (
        "ubicacion" in pregunta or "ubicación" in pregunta or "direccion" in pregunta or "dirección" in pregunta or
        "donde" in pregunta or "localizacion" in pregunta or "localización" in pregunta or "sede" in pregunta or "oficina" in pregunta
    ):
        hq = getattr(knowledge, "headquarters", None)
        if hq and hasattr(hq, "address"):
            respuestas.append(encabezado("Ubicación", f"Dirección: {hq.address}"))

    # Liderazgo
    if (
        "gerente" in pregunta or "general" in pregunta or "director" in pregunta or "jefe" in pregunta or "ejecutivo" in pregunta or "lider" in pregunta or "líder" in pregunta or "manager" in pregunta or "administrador" in pregunta
    ):
        ld = getattr(knowledge, "leadership", None)
        partes = []
        if ld:
            if hasattr(ld, "current_general_manager") and ld.current_general_manager:
                partes.append(f"Gerente general: {ld.current_general_manager}")
            if hasattr(ld, "other_key_executives") and ld.other_key_executives:
                otros = [f"{e.name} ({e.position})" for e in ld.other_key_executives if hasattr(e, "name") and hasattr(e, "position")]
                if otros:
                    partes.append(f"Otros ejecutivos: {', '.join(otros)}")
        if partes:
            respuestas.append(encabezado("Liderazgo", " | ".join(partes)))

    # Contacto
    if "teléfono" in pregunta or "telefono" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.phone} | Soporte técnico: {tech.phone}"))
        elif sales:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.phone}"))
        elif tech:
            respuestas.append(encabezado("Contacto", f"Soporte técnico: {tech.phone}"))
    if "email" in pregunta or "correo" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.email} | Soporte técnico: {tech.email}"))
        elif sales:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.email}"))
        elif tech:
            respuestas.append(encabezado("Contacto", f"Soporte técnico: {tech.email}"))
    if "horario" in pregunta or "atención" in pregunta or "atencion" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.hours} | Soporte técnico: {tech.hours}"))
        elif sales:
            respuestas.append(encabezado("Contacto", f"Ventas: {sales.hours}"))
        elif tech:
            respuestas.append(encabezado("Contacto", f"Soporte técnico: {tech.hours}"))
    if "sitio web" in pregunta or "web" in pregunta:
        hq = getattr(knowledge, "headquarters", None)
        if hq and hasattr(hq, "website"):
            respuestas.append(encabezado("Contacto", f"Sitio web: {hq.website}"))

    # Productos
    if "producto" in pregunta or "productos" in pregunta or "catálogo" in pregunta or "catalogo" in pregunta:
        ps = getattr(knowledge, "products_services", None)
        if ps:
            computo = getattr(ps, "computo", [])
            soluciones = getattr(ps, "soluciones_ti", [])
            perifericos = getattr(ps, "perifericos", [])
            respuestas.append(encabezado("Productos", f"Cómputo: {', '.join(computo)} | Soluciones TI: {', '.join(soluciones)} | Periféricos: {', '.join(perifericos)}"))

    # Distribuidores
    if (
        "distribuidor" in pregunta or "distribuidores" in pregunta or "mayorista" in pregunta or "retail" in pregunta or "partner" in pregunta or
        "canal" in pregunta or "canales" in pregunta or "red" in pregunta or "estrategia" in pregunta or "comercialización" in pregunta or "comercializacion" in pregunta or
        "reseller" in pregunta or "autorizado" in pregunta or "punto de venta" in pregunta or "venta" in pregunta
    ):
        dc = getattr(knowledge, "distribution_channels", None)
        if dc:
            mayorista = getattr(dc, "national_distributor", None)
            retail = getattr(dc, "retail_partners", [])
            estrategia = getattr(dc, "strategy", None)
            red = getattr(dc, "authorized_reseller_network", None)
            partes = []
            if estrategia:
                partes.append(f"Estrategia: {estrategia}")
            if mayorista:
                partes.append(f"Mayorista: {mayorista}")
            if retail:
                partes.append(f"Retail: {', '.join(retail)}")
            if red:
                partes.append(f"Red de resellers: {red}")
            if partes:
                respuestas.append(encabezado("Distribución", " | ".join(partes)))

    # Certificaciones
    if "certificación" in pregunta or "certificaciones" in pregunta:
        certs = getattr(knowledge, "certifications", [])
        if certs:
            respuestas.append(encabezado("Certificaciones", f"{', '.join(certs)}"))

    # Garantía
    if "garantía" in pregunta or "garantia" in pregunta:
        cc = getattr(getattr(knowledge, "products_services", None), "caracteristicas_clave", None)
        if cc and hasattr(cc, "garantia"):
            respuestas.append(encabezado("Garantía", f"{cc.garantia}"))

    # Historia
    if "historia" in pregunta or "evento" in pregunta or "fundación" in pregunta or "fundacion" in pregunta:
        ch = getattr(knowledge, "corporate_history", [])
        if ch and hasattr(ch[0], "event"):
            eventos = [f"{h.date}: {h.event}" for h in ch]
            respuestas.append(encabezado("Historia", "Eventos clave: " + "; ".join(eventos)))

    # Misión y visión
    if "misión" in pregunta or "mision" in pregunta:
        mv = getattr(knowledge, "mission_vision", None)
        if mv and hasattr(mv, "mission"):
            respuestas.append(encabezado("Misión", f"{mv.mission}"))
    if "visión" in pregunta or "vision" in pregunta:
        mv = getattr(knowledge, "mission_vision", None)
        if mv and hasattr(mv, "vision"):
            respuestas.append(encabezado("Visión", f"{mv.vision}"))

    # Alianzas
    if "alianza" in pregunta or "socios" in pregunta or "partners" in pregunta:
        al = getattr(knowledge, "alliances", [])
        if al:
            respuestas.append(encabezado("Alianzas", f"{', '.join(al)}"))

    # Segmentos de mercado
    if "segmento" in pregunta or "mercado" in pregunta or "clientes" in pregunta:
        mp = getattr(knowledge, "market_presence", None)
        if mp and hasattr(mp, "primary_segments"):
            respuestas.append(encabezado("Segmentos", f"{', '.join(mp.primary_segments)}"))

    # Si hay más de una respuesta, combinarlas de forma coherente
    if respuestas:
        return "\n---\n".join(respuestas)
    # Si no hay coincidencia, mostrar mensaje personalizado con ejemplos
    ejemplos = []
    # Ejemplo de productos
    ps = getattr(knowledge, "products_services", None)
    if ps:
        productos = []
        if hasattr(ps, "computo") and ps.computo:
            productos.append("computo")
        if hasattr(ps, "soluciones_ti") and ps.soluciones_ti:
            productos.append("soluciones TI")
        if hasattr(ps, "perifericos") and ps.perifericos:
            productos.append("periféricos")
        if productos:
            ejemplos.append(f"¿Qué productos de {', '.join(productos)} ofrece Vastec?")
    # Ejemplo de garantía
    cc = getattr(ps, "caracteristicas_clave", None) if ps else None
    if cc and hasattr(cc, "garantia") and cc.garantia:
        ejemplos.append("¿Cuál es la garantía de los productos?")
    # Ejemplo de ubicación
    hq = getattr(knowledge, "headquarters", None)
    if hq and hasattr(hq, "address") and hq.address:
        ejemplos.append("¿Dónde se ubica la oficina principal?")
    # Ejemplo de gerente general
    ld = getattr(knowledge, "leadership", None)
    if ld and hasattr(ld, "current_general_manager") and ld.current_general_manager:
        ejemplos.append("¿Quién es el gerente general?")
    # Ejemplo de canales de distribución
    dc = getattr(knowledge, "distribution_channels", None)
    if dc and (getattr(dc, "national_distributor", None) or getattr(dc, "retail_partners", None)):
        ejemplos.append("¿Cuáles son los canales de distribución?")
    # Ejemplo de certificaciones
    certs = getattr(knowledge, "certifications", [])
    if certs:
        ejemplos.append("¿Qué certificaciones tiene la empresa?")
    # Ejemplo de contacto
    contact = getattr(knowledge, "contact_information", None)
    if contact and (getattr(contact, "sales", None) or getattr(contact, "technical_support", None)):
        ejemplos.append("¿Cómo contactar a ventas o soporte técnico?")
    # Ejemplo de alianzas
    al = getattr(knowledge, "alliances", [])
    if al:
        ejemplos.append("¿Qué alianzas tecnológicas tiene Vastec?")
    # Ejemplo de sectores
    mp = getattr(knowledge, "market_presence", None)
    if mp and hasattr(mp, "primary_segments") and mp.primary_segments:
        ejemplos.append("¿Qué sectores atiende principalmente?")
    # Ejemplo de misión/visión
    mv = getattr(knowledge, "mission_vision", None)
    if mv and hasattr(mv, "mission") and mv.mission:
        ejemplos.append("¿Cuál es la misión de Vastec?")
    if mv and hasattr(mv, "vision") and mv.vision:
        ejemplos.append("¿Cuál es la visión de Vastec?")
    # Ejemplo de preguntas frecuentes
    faqs = getattr(knowledge, "frequently_asked_questions", [])
    if faqs:
        ejemplos.append("¿Cuáles son las preguntas frecuentes?")
    # Si no hay ejemplos, poner uno genérico
    if not ejemplos:
        ejemplos = ["¿Qué información tiene Vastec?"]
    mensaje = "No se tiene información sobre ese tema en la base de conocimiento. Puedes preguntar cualquier tema referente a Vastec y con gusto atenderé tu pedido.\nEjemplos de preguntas válidas:\n- " + "\n- ".join(ejemplos)
    return mensaje
    pregunta = pregunta.lower()
    # Contacto
    if "teléfono" in pregunta or "telefono" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            return f"Ventas: {sales.phone} | Soporte técnico: {tech.phone}"
        elif sales:
            return f"Ventas: {sales.phone}"
        elif tech:
            return f"Soporte técnico: {tech.phone}"
    if "email" in pregunta or "correo" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            return f"Ventas: {sales.email} | Soporte técnico: {tech.email}"
        elif sales:
            return f"Ventas: {sales.email}"
        elif tech:
            return f"Soporte técnico: {tech.email}"
    if "horario" in pregunta or "atención" in pregunta or "atencion" in pregunta:
        sales = getattr(getattr(knowledge, "contact_information", None), "sales", None)
        tech = getattr(getattr(knowledge, "contact_information", None), "technical_support", None)
        if sales and tech:
            return f"Ventas: {sales.hours} | Soporte técnico: {tech.hours}"
        elif sales:
            return f"Ventas: {sales.hours}"
        elif tech:
            return f"Soporte técnico: {tech.hours}"
    if "dirección" in pregunta or "direccion" in pregunta or "ubicación" in pregunta or "ubicacion" in pregunta:
        hq = getattr(knowledge, "headquarters", None)
        if hq and hasattr(hq, "address"):
            return f"Dirección: {hq.address}"
    if "sitio web" in pregunta or "web" in pregunta:
        hq = getattr(knowledge, "headquarters", None)
        if hq and hasattr(hq, "website"):
            return f"Sitio web: {hq.website}"
    # Productos
    if "producto" in pregunta or "productos" in pregunta or "catálogo" in pregunta or "catalogo" in pregunta:
        ps = getattr(knowledge, "products_services", None)
        if ps:
            computo = getattr(ps, "computo", [])
            soluciones = getattr(ps, "soluciones_ti", [])
            perifericos = getattr(ps, "perifericos", [])
            return f"Cómputo: {', '.join(computo)} | Soluciones TI: {', '.join(soluciones)} | Periféricos: {', '.join(perifericos)}"
    # Canales de distribución y variantes
    if (
        "distribuidor" in pregunta or "distribuidores" in pregunta or
        "mayorista" in pregunta or "retail" in pregunta or "partner" in pregunta or
        "canal" in pregunta or "canales" in pregunta or "red" in pregunta or
        "estrategia" in pregunta or "comercialización" in pregunta or "comercializacion" in pregunta or
        "reseller" in pregunta or "autorizado" in pregunta or "punto de venta" in pregunta or "venta" in pregunta
    ):
        dc = getattr(knowledge, "distribution_channels", None)
        if dc:
            mayorista = getattr(dc, "national_distributor", None)
            retail = getattr(dc, "retail_partners", [])
            estrategia = getattr(dc, "strategy", None)
            red = getattr(dc, "authorized_reseller_network", None)
            partes = []
            if estrategia:
                partes.append(f"Estrategia: {estrategia}")
            if mayorista:
                partes.append(f"Mayorista: {mayorista}")
            if retail:
                partes.append(f"Retail: {', '.join(retail)}")
            if red:
                partes.append(f"Red de resellers: {red}")
            if partes:
                return " | ".join(partes)
    # Certificaciones
    if "certificación" in pregunta or "certificaciones" in pregunta:
        certs = getattr(knowledge, "certifications", [])
        if certs:
            return f"Certificaciones: {', '.join(certs)}"
    # Garantía
    if "garantía" in pregunta or "garantia" in pregunta:
        cc = getattr(getattr(knowledge, "products_services", None), "caracteristicas_clave", None)
        if cc and hasattr(cc, "garantia"):
            return f"Garantía: {cc.garantia}"
    # Historia
    if "historia" in pregunta or "evento" in pregunta or "fundación" in pregunta or "fundacion" in pregunta:
        ch = getattr(knowledge, "corporate_history", [])
        if ch and hasattr(ch[0], "event"):
            eventos = [f"{h.date}: {h.event}" for h in ch]
            return "Eventos clave: " + "; ".join(eventos)
    # Preguntas frecuentes
    if "pregunta frecuente" in pregunta or "faq" in pregunta:
        faqs = getattr(knowledge, "frequently_asked_questions", [])
        if faqs and hasattr(faqs[0], "question"):
            preguntas = [f"{f.question}" for f in faqs]
            return "Preguntas frecuentes: " + "; ".join(preguntas)
    # Misión y visión
    if "misión" in pregunta or "mision" in pregunta:
        mv = getattr(knowledge, "mission_vision", None)
        if mv and hasattr(mv, "mission"):
            return f"Misión: {mv.mission}"
    if "visión" in pregunta or "vision" in pregunta:
        mv = getattr(knowledge, "mission_vision", None)
        if mv and hasattr(mv, "vision"):
            return f"Visión: {mv.vision}"
    # Alianzas
    if "alianza" in pregunta or "socios" in pregunta or "partners" in pregunta:
        al = getattr(knowledge, "alliances", [])
        if al:
            return f"Alianzas tecnológicas: {', '.join(al)}"
    # Segmentos de mercado
    if "segmento" in pregunta or "mercado" in pregunta or "clientes" in pregunta:
        mp = getattr(knowledge, "market_presence", None)
        if mp and hasattr(mp, "primary_segments"):
            return f"Segmentos principales: {', '.join(mp.primary_segments)}"
    return None
