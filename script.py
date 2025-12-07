from pathlib import Path
import re
text = Path('TRS_80_Model_100_Quick_Reference_Guide.extraction.md').read_text(encoding='utf-8', errors='ignore')
start = text.index('## BASIC Keywords (except for Input/output)')
end = text.index('## Keyboard Input Commands and Functions')
block = text[start:end]
lines = block.splitlines()
entries = []
current = None
for line in lines:
    line = line.rstrip()
    if not line:
        if current and current['description'] and current['description'][-1] != '':
            current['description'].append('')
        continue
    match = re.match(r'\*\*(.+?)\*\*(.*)', line)
    if match:
        if current:
            entries.append(current)
        name = match.group(1).strip()
        rest = match.group(2).strip()
        current = {'name': name, 'description': []}
        if rest:
            current['description'].append(rest)
    elif current:
        current['description'].append(line)
if current:
    entries.append(current)
with open('context/basic/keywords.md', 'w', encoding='utf-8') as out:
    out.write('# BASIC Keywords (except for Input/output)\n\n')
    for entry in entries:
        name = entry['name']
        out.write(f'### {name}\n')
        out.write(f'**Syntax:** `{name}`\n')
        if entry['description']:
            desc_lines = []
            paragraph = []
            for item in entry['description']:
                if item == '':
                    if paragraph:
                        desc_lines.append(' '.join(paragraph).strip())
                        paragraph = []
                else:
                    paragraph.append(item.strip())
            if paragraph:
                desc_lines.append(' '.join(paragraph).strip())
            for desc in desc_lines:
                if desc:
                    out.write(f'**Description:** {desc}\n')
        out.write('\n')
