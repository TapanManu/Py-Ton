list1=[input() for _ in range(10)]
list2=[]
for x in list1:
	if((x==1) and (x not in list2)):
		list2.append(x)	
	for i in range(1,x):
		if(x%i==0 and x/i==i):
			if x not in list2:
				list2.append(x)
print list2
