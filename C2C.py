import re
import time

changeTo = '_'
progressTmp = 0
def showProgress(percent):
	global progressTmp
	pstates = ('-', '\\', '|', '/')
	pstate = pstates[progressTmp]
	progressTmp += 1
	progressTmp %= 4
	tmp = "[" + pstate + "] ["
	for each in range(10):
		if percent > each :
			tmp += '#'	
		else:
			tmp += '-'
	tmp += ']'
	print(tmp, end = '\r')
	time.sleep(1)
	
file_name = input("请输入文件名:");
content = ''

showProgress(1)

words = set()
with open(file_name, "r") as file:
	for each in file:
		content += each
		if each.startswith("#"):
			continue
		mstr = each.replace("\n", "")
		mstr = re.sub(r'"([^"]|\")+"', " ", mstr)
		mstr = re.sub("\W", " ", mstr)
		mstr = re.sub("\\b\d+\\b", " ", mstr)
		mstr = re.sub("^\s+", "", mstr)
		mstr = re.sub("\s+$", "", mstr)
		mstr = re.sub("\s+", " ", mstr)
		marr = mstr.split(" ")
		for each in marr:
			words.add(each)

showProgress(2)

count = 0
aliases = {}
words.discard("")

showProgress(3)

for each in words:
	count += 1
	alias = ''
	for i in range(count):
		alias += changeTo
	aliases[each] = alias

showProgress(4)

for each in aliases:
	tmp = '\\b' + each + '\\b'
	content = re.sub(tmp, aliases[each], content)

showProgress(5)


for each in aliases:
	content = '#define ' + aliases[each] + ' ' +each + '\n' + content

showProgress(10)

with open("Ans.c", "w") as file:
	file.write(content)
