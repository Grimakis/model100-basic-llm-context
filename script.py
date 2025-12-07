from pathlib import Path
path = Path('context/basic/keywords.md')
lines = path.read_text(encoding='utf-8').splitlines()
new_lines = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith('**'):
        end = stripped.find('**', 2)
        if end != -1:
            name = stripped[2:end].strip()
            remainder = stripped[end+2:].strip()
            new_lines.append(f"### {name}")
            new_lines.append(f"**Syntax:** `{name}`")
            if remainder:
                new_lines.append(remainder)
            continue
    new_lines.append(line)
path.write_text('\n'.join(new_lines)+'\n', encoding='utf-8')
