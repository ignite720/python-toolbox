from pathlib import Path
import chardet
import codecs

def convert_text_file_encoding(oldfile, newfile, from_encoding="", to_encoding="utf-8-sig"):
    try:
        if from_encoding == "":
            with open(oldfile, "rb") as fp:
                from_encoding = chardet.detect(fp.read())["encoding"]
        print(f"{oldfile}, from encoding: {from_encoding}, to encoding: {to_encoding}")
        if from_encoding != to_encoding:
            with codecs.open(oldfile, "r", encoding=from_encoding) as fp:
                content = fp.read()
                
            with codecs.open(newfile, mode="w", encoding=to_encoding) as fp:
                fp.write(content)
    except Exception as e:
        print(e)
        
extensions = ("*.h", "*.cpp")

files = []
for e in extensions:
    files = (files + list(Path("./").rglob(e)))

for i in files:
    # eg. cp1252 is equivalent to Latin-1, cp936 is GBK, cp932 is Shift_JIS, cp949 is EUC-KR, respectively
    convert_text_file_encoding(i, i, "", "utf-8")