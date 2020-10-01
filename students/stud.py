stud = {}
marks = []
disp={}

for _ in range(5):
	name = input("enter the name of student:")
	print("enter marks of five subjects")
	marks=[]
	for i in range(5):
		marks.append(int(input("get mark:")))
	stud[name] = marks

for name,marks in stud.items():
	disp[name] = sum(marks)/len(marks)			#average calc and storing to another dict
	print(name," ",disp[name])

#print(disp)

t =[x for x in disp.values()]				#used list comprehension, can replace with loops
t.sort(reverse = True)
#print(t)

print("students with % marks\n")

while(len(t)!=0):
	x = t.pop(0)
	for key,value in disp.items():
		if(value==x):
			print(key,"=>",value)
