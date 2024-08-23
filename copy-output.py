import sys
import shutil
from pathlib import Path

def pathlib_copytree(srcDir, dstDir, extensions=("*.*",)):
    for ext in extensions:
        for fileFrom in Path(srcDir).rglob(ext):
            fileTo = (Path(dstDir) / fileFrom.name)
            fileTo.write_bytes(fileFrom.read_bytes())
            print(f"file has copied to {fileTo}")
    
srcDir = "./output"
dstDir = "../App/output"

if sys.version_info >= (3, 8):
    # dirs_exist_ok need python>=3.8
    shutil.copytree(srcDir, dstDir, dirs_exist_ok=True)
else:
    pathlib_copytree(srcDir, dstDir)
print("done")