#!/usr/bin/env python3
"""Generador de Poderes (Colombia) — modo hibrido.

Este helper implementa el skill "generador-poderes" descrito en SKILL.md.
Modos:
  - Plantilla en blanco:  python generar_poder.py <tipo> --plantilla
  - Entrevista guiada:    python generar_poder.py <tipo>   (pregunta lo esencial)
  - No interactivo:       python generar_poder.py <tipo> --set campo=valor ...

Tipos validos: general, especial, judicial, administrativo, maestra.

Redacta con lenguaje claro: encabezados descriptivos, resumen para el usuario no
experto y glosario de terminos legales. Cada plantilla cita su fundamento legal.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TIPOS = {
    "maestra": "references/plantilla-maestra.md",
    "general": "references/general.md",
    "especial": "references/especial.md",
    "judicial": "references/judicial.md",
    "administrativo": "references/administrativo.md",
}

# Texto de solemnidad por tipo.
SOLEMNIDAD = {
    "maestra": "Verifique la solemnidad segun el tipo de poder (escritura publica, "
               "autenticacion notarial o mensaje de datos judicial).",
    "general": "Escritura Publica ante Notario (ad solemnitatem). Desde el exterior: "
               "consul colombiano o notaria extranjera con apostilla/legalizacion (art. 251 CGP).",
    "especial": "Para inmuebles: Escritura Publica. Para gestiones menores: documento "
                "privado con presentacion personal y autenticacion notarial.",
    "judicial": "Ley 2213 de 2022 (Justicia Digital): mensaje de datos sin firma manuscrita; "
                "basta la antefirma. Persona juridica: correo corporativo de Camara de Comercio.",
    "administrativo": "Documento privado original con presentacion personal y validacion "
                      "biometrica ante Notario. Ley 2213/2022 NO aplica. Alternativa: firma "
                      "digital certificada (Ley 527/1999). Ante DIAN: abogado inscrito.",
}

# Notas de revocacion por defecto (editables en entrevista).
REVOCACION = {
    "maestra": "Podra revocar este poder en cualquier momento notificando al apoderado.",
    "general": "Se revoca mediante nueva Escritura Publica de Revocacion notificada al apoderado y terceros.",
    "especial": "Mediante documento privado de revocatoria entregado al apoderado y a las entidades.",
    "judicial": "Mediante memorial de revocatoria radicado ante el juez de la causa.",
    "administrativo": "Mediante comunicacion escrita al apoderado y a la entidad publica correspondiente.",
}

# Glosario comun (define tecnicismos y siglas la primera vez).
GLOSARIO = (
    "- **Cedula de ciudadania / extranjeria:** documento de identidad colombiano.\n"
    "- **Escritura publica:** documento firmado ante notario con plena fe juridica.\n"
    "- **Matricula inmobiliaria:** numero unico que identifica un predio en el Registro.\n"
    "- **Chip / cedula catastral:** codigo del predio ante el Catastro.\n"
    "- **Tarjeta profesional:** identificacion del abogado ante el Consejo Superior de la Judicatura.\n"
    "- **Apostilla / legalizacion:** validacion de un documento extranjero para Colombia (art. 251 CGP).\n"
    "- **CGP:** Codigo General del Proceso (Ley 1564 de 2012).\n"
    "- **DIAN:** Direccion de Impuestos y Aduanas Nacionales.\n"
    "- **RNA / SIRNA:** Registro Nacional de Abogados.\n"
    "- **Ley 2213 de 2022:** Justicia Digital; permite poderes judiciales por mensaje de datos.\n"
    "- **Ley 527 de 1999:** firma digital certificada.\n"
)

# Definicion de campos por tipo. (token, prompt, requerido, validador)
def _email(v):
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", v):
        raise ValueError("correo no valido")
    return v

def _doc(v):
    if not re.match(r"^[0-9A-Za-z.\-]{3,}$", v):
        raise ValueError("documento no valido (use solo digitos/letras)")
    return v

COMUN = [
    ("poderdante_nombre", "Nombre completo del poderdante", True, None),
    ("poderdante_doc_tipo", "Tipo de documento del poderdante (C.C./C.E./Pasaporte)", True, None),
    ("poderdante_doc", "Numero de documento del poderdante", True, _doc),
    ("poderdante_edad", "Edad del poderdante", True, None),
    ("poderdante_domicilio", "Domicilio del poderdante", True, None),
    ("apoderado_nombre", "Nombre completo del apoderado", True, None),
    ("apoderado_doc_tipo", "Tipo de documento del apoderado (C.C./C.E./Pasaporte/T.P.)", True, None),
    ("apoderado_doc", "Numero de documento del apoderado", True, _doc),
    ("apoderado_domicilio", "Domicilio del apoderado", True, None),
    ("ciudad", "Ciudad", True, None),
    ("notaria", "Notaria o autoridad de destino", True, None),
    ("fecha", "Fecha (AAAA-MM-DD)", True, None),
    ("facultades", "Facultades otorgadas (texto libre; sea especifico)", True, None),
    ("vigencia", "Vigencia (plazo o 'indefinida')", True, None),
]

EXTRA = {
    "judicial": [
        ("tarjeta_profesional", "Tarjeta profesional del abogado", True, None),
        ("correo_rna", "Correo del abogado (debe coincidir con RNA/SIRNA)", True, _email),
        ("despacho", "Despacho de conocimiento", False, None),
        ("partes", "Partes involucradas", False, None),
        ("objeto_litigio", "Objeto del litigio", False, None),
        ("facultades_extraordinarias", "Facultades de disposicion extraordinaria (listar expresas)", False, None),
    ],
    "especial": [
        ("nomenclatura", "Nomenclatura del inmueble (si aplica)", False, None),
        ("matricula", "Matricula inmobiliaria (si aplica)", False, None),
        ("chip", "Cedula catastral/chip (si aplica)", False, None),
        ("escritura_vendedor", "Escritura de adquisicion del vendedor (si aplica)", False, None),
    ],
}


def campos(tipo):
    fs = list(COMUN)
    for t, extra in EXTRA.items():
        if t == tipo:
            fs += extra
    return fs


def cargar_plantilla(tipo):
    return (HERE / TIPOS[tipo]).read_text(encoding="utf-8")


def render(tipo, valores):
    texto = cargar_plantilla(tipo)
    sustituciones = dict(valores)
    sustituciones.setdefault("solemnidad", SOLEMNIDAD[tipo])
    sustituciones.setdefault("glosario", GLOSARIO)
    sustituciones.setdefault("revocacion_notas", REVOCACION[tipo])
    for tok, val in sustituciones.items():
        texto = texto.replace("{{%s}}" % tok, val if val is not None else "")
    faltantes = re.findall(r"\{\{(\w+)\}\}", texto)
    if faltantes:
        texto += "\n\n> **Campos sin rellenar:** " + ", ".join(sorted(set(faltantes))) + "\n"
    return texto


def modo_plantilla(tipo):
    texto = cargar_plantilla(tipo)
    return re.sub(r"\{\{(\w+)\}\}", r"[\1]", texto)


def preguntar(tipo, prefijos):
    valores = {}
    for tok, prompt, requerido, validador in campos(tipo):
        if tok in prefijos:
            valores[tok] = prefijos[tok]
            continue
        while True:
            sufijo = " (requerido): " if requerido else " (opcional, Enter para omitir): "
            resp = input(prompt + sufijo).strip()
            if not resp:
                if requerido:
                    print("  -> Este campo es requerido.")
                    continue
                resp = ""
            if validador:
                try:
                    validador(resp)
                except ValueError as e:
                    print("  -> Error:", e)
                    continue
            valores[tok] = resp
            break
    return valores


def main():
    ap = argparse.ArgumentParser(description="Generador de Poderes (Colombia)")
    ap.add_argument("tipo", choices=list(TIPOS.keys()))
    ap.add_argument("--plantilla", action="store_true", help="Imprime la plantilla en blanco")
    ap.add_argument("--output", help="Archivo de salida (en vez de stdout)")
    ap.add_argument("--set", action="append", default=[], help="campo=valor (no interactivo)")
    args = ap.parse_args()

    if args.plantilla:
        salida = modo_plantilla(args.tipo)
    else:
        prefijos = {}
        for s in args.set:
            if "=" in s:
                k, v = s.split("=", 1)
                prefijos[k.strip()] = v.strip()
        if prefijos or not sys.stdin.isatty():
            valores = {k: v for k, v in prefijos.items()}
            for tok, _, requerido, _ in campos(args.tipo):
                valores.setdefault(tok, "")
            salida = render(args.tipo, valores)
        else:
            valores = preguntar(args.tipo, prefijos)
            salida = render(args.tipo, valores)

    if args.output:
        Path(args.output).write_text(salida, encoding="utf-8")
        print("Guardado en", args.output)
    else:
        print(salida)


if __name__ == "__main__":
    main()
