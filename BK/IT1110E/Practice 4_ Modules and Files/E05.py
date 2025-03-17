from collections import Counter
import re

with open('test.inp', 'r') as f:
    text = f.read()
words = re.findall(r'[^\s]+(?:\n|\s*)', text)
with open('test.out', 'w') as f:
    f.write(str(dict(Counter(words))))
with open('test.out', 'r') as f:
	all = f.read()
	print(all)
f.close()