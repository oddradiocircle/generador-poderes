---
name: generador-poderes
description: >-
  Genera poderes (powers of attorney) colombianos a partir de plantillas
  fundamentadas en la legislacion local, para abogados y cualquier persona que
  entienda que es un poder y quiera crear uno, de cualquier tipo. Aplica lenguaje
  claro y valida campos obligatorios. Usa cuando el usuario pida redactar, generar
  o hacer un poder, mandato o representacion en Colombia, o mencione "poder
  especial", "poder judicial", "poder general" o "poder administrativo".
metadata:
  author: oddradiocircle
  version: "1.0.0"
---

# Generador de Poderes (Colombia)

Genera documentos de poder de representacion colombianos en **Markdown limpio**,
listos para pasar a Word/PDF y luego autenticar ante la autoridad competente.

## Cuando usar este skill
- El usuario pide "hacer un poder", "generar un mandato", "redactar un poder
  especial/judicial/administrativo/general" en Colombia.
- El usuario es abogado o cualquier persona que entienda el concepto de poder.

## Modo hibrido (como opera)
1. **Entrevista guiada (por defecto):** haz preguntas claras una a una para
   obtener lo esencial (tipo, datos de poderdante y apoderado, facultades,
   vigencia, revocacion, notas). Usa lenguaje claro.
2. **Modo solo plantilla:** si el usuario solo quiere el esqueleto, entrega la
   plantilla con campos en blanco `[...]`.

Puedes invocar el helper (Python, solo biblioteca estandar):
```bash
# Plantilla en blanco
python scripts/generar_poder.py <tipo> --plantilla

# Entrevista guiada (en terminal)
python scripts/generar_poder.py <tipo>

# No interactivo (valores directos)
python scripts/generar_poder.py <tipo> --set poderdante_nombre="..." --set ...
```
Tipos: `general`, `especial`, `judicial`, `administrativo`, `maestra`.

Tambien puedes copiar la plantilla de `references/<tipo>.md` y rellenar los
campos `{{...}}` directamente, conservando las capas de claridad.

## Tipos de poder (base legal)
- **general** — amplio y suficiente; **Escritura Publica** ante Notario
  (ad solemnitatem). Solo concede administracion ordinaria; la disposicion
  extraordinaria (vender/hipotecar/donar inmuebles) debe listarse expresa.
- **especial** — un negocio concreto (compraventa de inmueble, asamblea,
  matrimonio). Exige determinacion formal del inmueble si aplica.
- **judicial** — pleitos y cobranzas; abogado con Tarjeta Profesional y correo
  RNA/SIRNA. Ley 2213 de 2022 permite mensaje de datos sin firma manuscrita.
- **administrativo** — gestiones ante entidades publicas (DIAN, alcaldias,
  registro/catastro, transito, SECOP II). Documento privado con validacion
  biometrica notarial; Ley 2213 NO aplica. Ante DIAN: abogado inscrito.

## Reglas de calidad (lenguaje claro) — +calidad +precision +confianza
- **Juridico:** encabezados descriptivos, introduccion de proposito por
  seccion, y **capas de informacion**: un resumen en lenguaje claro para el no
  experto + el texto formal. Revisa la plantilla antes de reutilizarla.
- **Tecnicismos:** explica terminos legales la primera vez que aparecen
  y desarrolla siglas (CGP, DIAN, RNA/SIRNA, Ley 2213/2022, Ley 527/1999). Ver
  seccion "Glosario" al pie de cada plantilla.
- **Principios:** Relevancia (solo clausulas del tipo), Localizabilidad
  (estructura + encabezados), Comprensibilidad (palabras familiares, oraciones
  cortas), Usabilidad (el usuario puede completar y usar el documento).

## Validacion
Antes de entregar, verifica campos obligatorios:
- Siempre: nombres completos y documentos de poderdante y apoderado.
- **judicial:** Tarjeta Profesional vigente y correo que coincida con RNA/SIRNA.
- **especial con inmueble:** nomenclatura, matricula inmobiliaria y chip.

## Avisos obligatorios
- Inserta el aviso de **solemnidad** segun el tipo (ver seccion "Solemnidad" de
  la plantilla en `references/<tipo>.md`).
- Inserta el **aviso de borrador**: "Este documento es un borrador generado por un
  asistente. No es asesoria juridica. Debe revisarse y autenticarse ante la
  autoridad competente."

## Fuentes
- Cada plantilla cita su fundamento (Codigo Civil, Decreto 960/1970, CGP arts.
  74/77, Ley 2213/2022, Ley 527/1999).
