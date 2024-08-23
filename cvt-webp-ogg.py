from pathlib import Path
import os

extensions = ("*.wav", "*.png")
files = []
for e in extensions:
    files = (files + list(Path("./").rglob(e)))

for i in files:
    print(i)
    
    cmd = ""
    if i.suffix == ".png":
        cmd = f"cwebp.exe {i} -o {i.parent / i.stem}.webp"
    elif i.suffix == ".wav":
        cmd = f"oggenc2.exe {i} -o {i.parent / i.stem}.ogg"
    os.system(cmd)
    
    # warning: please back up your files first
    #i.unlink()