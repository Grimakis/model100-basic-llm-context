from pathlib import Path
import re
text = Path('TRS_80_Model_100_Quick_Reference_Guide.extraction.md').read_text(encoding='utf-8', errors='ignore')
start = text.index('## BASIC Keywords (except for Input/output)')
end = text.index('## Keyboard Input Commands and Functions')
block = text[start:end]
entries = []
current = None
for line in block.splitlines():
    stripped = line.strip()
    if not stripped:
        continue
    new_entry_match = re.match(r'^\*\*(?!Description:|Examples:)([^*]+?)\*\*(.*)$', stripped)
    if new_entry_match:
        if current:
            entries.append(current)
        name = new_entry_match.group(1).strip()
        remainder = new_entry_match.group(2).strip()
        current = {'name': name, 'lines': []}
        if remainder:
            current['lines'].append(remainder)
        continue
    if current is None:
        continue
    cleaned = re.sub(r'<a[^>]*>', '', stripped)
    cleaned = re.sub(r'</a>', '', cleaned)
    cleaned = re.sub(r'<!--.*?-->', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    if cleaned:
        current['lines'].append(cleaned)
if current:
    entries.append(current)
with open('context/basic/keywords.md', 'w', encoding='utf-8') as out:
    out.write('# BASIC Keywords (except for Input/output)\n\n')
    for entry in entries:
        name = entry['name']
        description = ' '.join(entry['lines']).strip()
        out.write(f'### {name}\n')
        out.write(f'**Syntax:** `{name}`\n')
        if description:
            out.write(f'**Description:** {description}\n')
        out.write('\n')
