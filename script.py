from pathlib import Path
import re, html
text = Path('context/ascii.md').read_text(encoding='utf-8', errors='ignore')
rows = re.findall(r'<tr>(.*?)</tr>', text, re.S)
data = []
for row in rows:
    cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
    if len(cells) != 5:
        continue
    data.append([html.unescape(cell.strip().replace('\n', ' ').replace('\r', ' ').strip()) for cell in cells])
if not data:
    raise SystemExit('No rows found')
chunks = []
for start in range(0, len(data), 32):
    chunk = data[start:start+32]
    if not chunk:
        continue
    section = []
    section.append(f"## Decimal {start}-{start+len(chunk)-1}")
    section.append('')
    section.append('| Decimal | Hex | Binary | Printed Character | Keyboard Character |')
    section.append('| --- | --- | --- | --- | --- |')
    for row in chunk:
        section.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")
    chunks.append('\n'.join(section))
output = '# ASCII Codes/Characters\n\n' + '\n\n'.join(chunks) + '\n'
Path('context/ascii.md').write_text(output, encoding='utf-8')
