# Model 100 BASIC LLM Context

This repository packages the TRS-80 Model 100 Quick Reference content as reusable context snippets for LLM coding agents (Copilot, Claude Code, etc.).

## Structure
- `context/00-overview.md`: guide usage, function-key table, power/menu tips.
- `context/text-editor.md`, `context/scheduler.md`, `context/address.md`, `context/telecommunications.md`: front-line application references.
- `context/sound-generator.md`, `context/ascii.md`, `context/basic-error-codes.md`: reference tables for tone commands, ASCII/keyboard, and BASIC error codes.
- `context/basic/`: detailed BASIC-focused commands for interpreter keys, keywords, keyboard input, screen/printer, RAM, cassette, and communications. Each file already uses per-command headings plus syntax descriptions.

## Usage
1. Clone or download this repo.
2. Point your LLM tooling to the relevant file(s) via the plugin’s context panel, prompt helper, or retrieval layer so the specific commands are visible within the agent’s working context.
3. When working on a project, import the folders once and refer to the raw Markdown (or embed excerpts) instead of copying sections between repos.

## Syncing to Your Workflow
You can keep this repo in a shared location and configure your agent (e.g., via a shell script or plugin setting) to copy relevant files into the current workspace, or to pass the raw text by URL into the prompt before asking for help.
