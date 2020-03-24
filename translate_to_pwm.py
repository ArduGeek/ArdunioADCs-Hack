import numpy as np

text = open("./pwm.txt")
string = text.read()
text.close()
lines = string.splitlines()
values = []
result = []
counter = 0;
for i in lines:
	values.append(float(i))	
for i in values:
	counter += 1
	result.append(int(round(np.interp
	(i,[-1,1],[0,255]),0)))
print(result)
