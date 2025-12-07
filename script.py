from pathlib import Path
import re
text = Path('TRS_80_Model_100_Quick_Reference_Guide.extraction.md').read_text(encoding='utf-8', errors='ignore')
start = text.index('## BASIC Keywords (except for Input/output)')
end = text.index('## Keyboard Input Commands and Functions')
block = text[start:end]
items = re.split(r'(?=\*\*[^\n]+\*\*)', block)
entries = []
for item in items:
    item = item.strip()
    if not item:
        continue
    first = re.match(r'\*\*(.+?)\*\*\s*(.*)', item, re.S)
    if not first:
        continue
    name = first.group(1).strip()
    rest = first.group(2).strip()
    rest = re.sub(r'<a[^>]+>', '', rest)
    rest = re.sub(r'\s+', ' ', rest)
    entries.append((name, rest.strip()))
with open('context/basic/keywords.md', 'w', encoding='utf-8') as out:
    out.write('# BASIC Keywords (except for Input/output)\n\n')
    for name, desc in entries:
        out.write(f'### {name}\n')
        out.write(f'**Syntax:** `{name}`\n')
        if desc:
            out.write(f'**Description:** {desc}\n')
        out.write('\n')
