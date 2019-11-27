f=open("essay2.txt",'r')
count=0
for lines in f:
	text=lines.split()
	for _ in text:
		count+=1

print("total no of words:",count)
f.close()
