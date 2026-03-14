import os
import re
import sys

from pathlib import Path


app__path = Path(__file__).resolve().parent
source_root = app__path.parent
print(f"Source Root: {source_root}")

x = input("This script will patch the source files for better compatibility with modern tools. Do you want to proceed? (y/n): ")
if x.lower() != 'y':
    print("Aborting patching process.")
    sys.exit(0)

else:
    os.chdir(source_root)
    

# 1. SETENV.BAT Patchen
setenv = Path("SETENV.BAT")
if setenv.exists():
    content = setenv.read_text(encoding="ascii", errors="ignore")
    content = content.replace(r"tools\lib", r"tools\bld\lib")
    content = content.replace(r"tools\inc", r"tools\bld\inc")
    setenv.write_text(content, encoding="ascii")

# 2. Sonderzeichen in ASM/INF Dateien fixen
fix_files = ["MAPPER/GETMSG.ASM", "SELECT/SELECT2.ASM", "SELECT/USA.INF"]
# Regex für die kaputten Zeichen (UTF-8 Trümmer)
pattern = re.compile(r"(\xef\xbf\xbd|\xc4\xbf|\xc4\xb4)")

for file_path in fix_files:
    path = Path(file_path)
    if path.exists():
        # Wir lesen es binär, um Encoding-Fehler beim Suchen zu vermeiden
        data = path.read_bytes()
        # Ersetze die Byte-Folgen durch das ASCII-Zeichen '#' (0x23)
        data = data.replace(b'\xef\xbf\xbd', b'#').replace(b'\xc4\xbf', b'#').replace(b'\xc4\xb4', b'#')
        path.write_bytes(data)

# 3. CRLF Normalisierung für DOS-Kompatibilität
extensions = ['*.BAT', '*.ASM', '*.SKL', 'ZERO.DAT', 'LOCSCR']
for ext in extensions:
    for file in Path(".").rglob(ext):
        print(f"Fixing Line Endings: {file}")
        content = file.read_bytes()
        # Verhindert doppelte \r\r\n: Erst alle \r entfernen, dann \n zu \r\n
        content = content.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
        file.write_bytes(content)