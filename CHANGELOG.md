# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [0.1.1] - 2026-08-22

### Changed
- Docs: README reescrito con Markdown de GitHub al máximo — badges (skills.sh, release, license), alerts `[!TIP]`/`[!NOTE]`/`[!IMPORTANT]`/`[!CAUTION]`, `<details>` colapsable para "Sin consola", tablas para instalación manual y tipos de poder, bloque copiable del prompt y footer centrado.

## [0.1.0] - 2026-08-22

### Added
- Release inicial del skill **generador-poderes** para poderes colombianos.
- 5 plantillas en `skills/generador-poderes/`: `maestra` (base), `general`, `especial`, `judicial`, `administrativo` — en Markdown limpio con lenguaje claro, glosario y avisos de solemnidad.
- Helper `scripts/generar_poder.py` (solo stdlib): modo plantilla en blanco, entrevista guiada y `--set campo=valor` con validación de campos obligatorios.
- `SKILL.md` conforme al formato de skills (name/description/metadata) y `plugin.json` para indexado en skills.sh.
- Instalación genérica: `npx skills add oddradiocircle/generador-poderes` y copia manual en `~/.claude/skills/` (macOS/Linux) y `%USERPROFILE%\.claude\skills\` (Windows).
- Prompt de instalación automática para agentes (estilo Vercel).
- Licencia MIT y documentación de uso/estructura.
