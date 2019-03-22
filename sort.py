a=[]
b=[]
c=[]
n=int(input("enter the range"))     
for _ in range(n):
     lst=[]
     name=input("enter the name:")
     score=float(input("enter the mark"))
     lst.append(name)
     lst.append(score)
     b.append(score)		
     a.append(lst)
a.sort()
b.sort()    
print(a,)
print(b,)
for i in range(n):
	if(b[i]>b[0]):
		target=b[i]
		break
for i in range(n):
	if(a[i][1]==target):
		c.append(a[i][0])
for k in c:
	print (k)




