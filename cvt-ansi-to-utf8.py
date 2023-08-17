from pathlib import Path
import chardet
import codecs

def convert_ansi_to_utf8(oldfile, newfile, fromEncoding=""):
	try:
		if fromEncoding == "":
			with open(oldfile, "rb") as fp:
				fromEncoding = chardet.detect(fp.read())["encoding"]
		print(f"{oldfile}, encoding: {fromEncoding}")
		
		with codecs.open(oldfile, "r", encoding=fromEncoding) as fp:
			content = fp.read()
			
		with codecs.open(newfile, mode="w", encoding="utf_8_sig") as fp:
			fp.write(content)
	except Exception as e:
		print(e)
		
extensions = ("*.h", "*.cpp")
files = []
for e in extensions:
	files = (files + list(Path("./").rglob(e)))

for i in files:
	# eg. cp1252 is equivalent to Latin-1, cp936 is GBK, cp932 is Shift_JIS, cp949 is EUC-KR, respectively
	convert_ansi_to_utf8(i, i, "cp932")