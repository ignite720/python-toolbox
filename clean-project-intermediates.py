from pathlib import Path
import shutil
import os

dirToRemove = (Path("./fooproject") / "x64")
try:
	shutil.rmtree(dirToRemove)
except Exception as e:
	print(f"{str(type(e))}: {e}")

extensions = ("*.exe", "*.pdb")
files = []
for e in extensions:
	files = (files + list(Path("./x64").rglob(e)))

for file in files:
	print(file)
	os.remove(file)