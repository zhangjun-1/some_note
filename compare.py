
#!/usr/bin/python
import difflib
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1,'rb') as text1:
    text1_lines = text1.read().decode().splitlines()
with open(filename2,'rb') as text2:
    text2_lines = text2.read().decode().splitlines()

d = difflib.HtmlDiff()
a = d.make_file(text1_lines,text2_lines)
with open('diff.html','w',encoding='utf-8') as diff_file:
    diff_file.write(a)
