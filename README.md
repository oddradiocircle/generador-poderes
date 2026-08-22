# generador-poderes

[![skills.sh](https://skills.sh/b/oddradiocircle/generador-poderes)](https://www.skills.sh/oddradiocircle/generador-poderes) [![Release](https://img.shields.io/github/v/release/oddradiocircle/generador-poderes?label=release)](https://github.com/oddradiocircle/generador-poderes/releases/tag/v0.1.0) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Genera poderes (powers of attorney) colombianos en Markdown limpio** — plantillas fundamentadas en la legislación local, con lenguaje claro, validación y glosario. Listo para Word/PDF y autenticación notarial.

> [!TIP]
> **Compatible con todo el ecosistema abierto de skills:** Claude Code · Claude Cowork · Cursor · Codex · GitHub Copilot · Windsurf · Gemini · Cline y 80+ agentes vía `npx skills`.

## ⚡ Instalación en 10 segundos

### 🤖 Prompt automático (recomendado)

> [!NOTE]
> Copia y pega este prompt en tu agente — él lo instala solo:

```text
Usa los skills en "oddradiocircle/generador-poderes" que sean relevantes para la tarea actual. Ejecuta `npx skills add oddradiocircle/generador-poderes` y selecciona los skills relevantes, luego sigue sus instrucciones.
```

<details>
<summary>🖱️ Sin consola — copia manual</summary>

Si no quieres usar la terminal, copia la carpeta `generador-poderes` a `~/.claude/skills/generador-poderes/` con el explorador de archivos. Cero comandos.

Ver detalles en [Instalación manual](#-instalación-manual--sin-cli) abajo.

</details>

### 🛠️ CLI — una línea

```bash
npx skills add oddradiocircle/generador-poderes
```

¿Tienes la carpeta local? También vale:

```bash
npx skills add ./generador-poderes
```

## 📥 Instalación manual — sin CLI

> [!IMPORTANT]
> Los skills de Claude son carpetas. Solo cópialas a la carpeta de skills.

| Plataforma | Destino personal (todos tus proyectos) | Por proyecto |
| :--- | :--- | :--- |
| **macOS / Linux** | `~/.claude/skills/generador-poderes/` <br> `cp -r generador-poderes ~/.claude/skills/` | `<proyecto>/.claude/skills/generador-poderes/` |
| **Windows (PowerShell)** | `%USERPROFILE%\.claude\skills\generador-poderes\` <br> `Copy-Item -Recurse generador-poderes $env:USERPROFILE\.claude\skills\` | `<proyecto>\.claude\skills\generador-poderes\` |

> [!NOTE]
> Si la carpeta `.claude/skills/` no existía al iniciar Claude Code, reinicia la sesión.

## 📖 Uso

Pide al agente:

- “redacta un poder especial para vender el inmueble matrícula X”
- “genera un poder judicial para el abogado Y”

O usa el helper (Python, solo stdlib):

```bash
# Plantilla en blanco
python skills/generador-poderes/scripts/generar_poder.py general --plantilla

# No interactivo
python skills/generador-poderes/scripts/generar_poder.py judicial --set poderdante_nombre="María López" --set ...
```

| Tipo | Uso |
| :--- | :--- |
| `general` | Amplio y suficiente — escritura pública |
| `especial` | Negocio concreto (inmueble, asamblea) |
| `judicial` | Pleitos — abogado con T.P. y correo RNA/SIRNA |
| `administrativo` | DIAN, alcaldías, registro, tránsito, SECOP II |
| `maestra` | Base configurable |

## 📂 Estructura

```text
generador-poderes/
├── plugin.json
├── skills/generador-poderes/
│   ├── SKILL.md
│   ├── scripts/generar_poder.py
│   └── references/<tipo>.md
├── CHANGELOG.md
└── LICENSE
```

## ⚠️ Aviso

> [!CAUTION]
> Este skill produce **borradores**. No constituye asesoría jurídica. Debe revisarse por abogado o autenticarse ante la autoridad competente segun correspanda a cada caso.

---

<div align="center">

**Hecho con lenguaje claro para Colombia 🇨🇴**

[Releases](https://github.com/oddradiocircle/generador-poderes/releases) · [Reportar issue](https://github.com/oddradiocircle/generador-poderes/issues) · [skills.sh](https://www.skills.sh/oddradiocircle/generador-poderes)

</div>
