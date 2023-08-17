from pathlib import Path
import codecs

def convert_utf8_to_ansi2(oldfile, newfile):
	with open(oldfile, "r", encoding="utf_8_sig") as fp:
		content = fp.read()
	with open(newfile, mode="w", encoding="cp936") as fp:
		fp.write(content)
	
def convert_utf8_to_ansi(oldfile, newfile):
	try:
		with codecs.open(oldfile, "r", encoding="utf_8_sig") as fp:
			content = fp.read()
			
		with codecs.open(newfile, mode="w", encoding="cp936") as fp:
			fp.write(content)
	except Exception as e:
		print(e)
		
extensions = ("*.h", "*.cpp")
files = []
for e in extensions:
	for item in Path("./").rglob(e):
		files.append(item)

for i in files:
	print(i)
	convert_utf8_to_ansi(i, i)