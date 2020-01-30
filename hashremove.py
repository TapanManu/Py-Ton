f1=open("male_cricketers.py",'r')
f2=open("male_cricketer.py",'w')
for line in f1:
	if not line.startswith('#'):
		f2.write(line)
f1.close()
f2.close()
