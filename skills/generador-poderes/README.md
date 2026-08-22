# generador-poderes

Skill para agentes de IA que genera **poderes (powers of attorney) colombianos**
en Markdown, a partir de plantillas fundamentadas en la legislacion local.
Aplica lenguaje claro y valida los campos obligatorios.

Este skill funciona en cualquier agente que soporte el formato abierto de skills
(Claude Code, Claude Cowork, Cursor, Codex, GitHub Copilot, Windsurf, Gemini,
Cline y 80+ mas).

## Prompt de instalacion automatica (para darle a tu agente)

Copia y pega este prompt en la conversacion de tu agente (Claude Code, Cursor,
Codex, Copilot, etc.) y el agente lo instalara solo:

---
Usa los skills en "https://github.com/oddradiocircle/generador-poderes" que sean
relevantes para la tarea actual. Ejecuta
`npx skills add "https://github.com/oddradiocircle/generador-poderes"` y selecciona
los skills relevantes, luego sigue sus instrucciones.
---

> **Sin consola:** si no quieres usar la terminal, omite este prompt y ve a la
> seccion "Instalacion manual en Claude (Windows y macOS) — sin CLI" (abajo):
> solo copia la carpeta del skill a `~/.claude/skills/generador-poderes/` con el
> explorador de archivos. Cero linea de comandos.

## Instalacion con el CLI skills (la forma mas simple)

No necesitas indicar el agente: el CLI lo detecta e instala en su carpeta de
skills automaticamente. Apunta al repositorio de GitHub (ya publicado):

```bash
npx skills add "https://github.com/oddradiocircle/generador-poderes"
```

Si tienes la carpeta del skill localmente, tambien puedes usar la ruta:
```bash
npx skills add ./generador-poderes
```

## Instalacion manual en Claude (Windows y macOS) — sin CLI

Los skills de Claude Code son simples carpetas. Solo copia el skill a la carpeta
de skills de Claude; no necesitas el CLI.

**macOS / Linux (personal, disponible en todos tus proyectos):**
```bash
cp -r generador-poderes ~/.claude/skills/
# Queda en: ~/.claude/skills/generador-poderes/
```

**Windows (PowerShell, personal):**
```powershell
Copy-Item -Recurse generador-poderes $env:USERPROFILE\.claude\skills\
# Queda en: %USERPROFILE%\.claude\skills\generador-poderes\
```

**Por proyecto** (en la raiz de tu proyecto, en vez de tu home):
- macOS/Linux: `<proyecto>/.claude/skills/generador-poderes/`
- Windows: `<proyecto>\.claude\skills\generador-poderes\`

> Si la carpeta `.claude/skills/` no existia cuando iniciaste Claude Code,
> reinicia la sesion para que la detecte.

## Uso

Pide al agente algo como: "redacta un poder especial para vender el inmueble
matricula X", "genera un poder judicial para el abogado Y", etc.

El agente puede usar el helper incluido (Python, solo biblioteca estandar):

```bash
python scripts/generar_poder.py <tipo> --plantilla          # plantilla en blanco
python scripts/generar_poder.py <tipo> --set campo=valor   # no interactivo
```

Tipos: `general`, `especial`, `judicial`, `administrativo`, `maestra`.

## Estructura

```
generador-poderes/
  SKILL.md                     # metadatos + instrucciones
  scripts/generar_poder.py     # generador (solo stdlib)
  references/<tipo>.md         # plantillas por tipo
  LICENSE
  README.md
```

## Aviso

Este skill produce borradores. No constituye asesoria juridica. Los documentos
deben revisarse y autenticarse ante la autoridad competente.
