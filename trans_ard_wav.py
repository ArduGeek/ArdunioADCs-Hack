import numpy as np


text = open("./input.txt")
string = text.read()
text.close()
lines = string.splitlines()
values = []
result = []
counter = 0;
for i in lines:
	values.append(int(i))	
for i in values:
	counter += 1
	result.append(int(round(np.interp
	(i,[0,1024],[-32768,32768]),0)))
for i in result:
	print(i)
