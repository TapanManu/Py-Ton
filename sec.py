arr=[]
for _ in range(5):
	arr.append(raw_input())
list=[]
count=1
seclarge=0
for i in arr:
	if i not in list:
        	list.append(i)
list.sort(reverse=True)
for i in range(1,len(list)-1):
        if(list[i-1:i]!=list[i:i+1]):
        	seclarge=list[i:i+1]
		print(seclarge)
		break
        else:
        	count+=1
if(count==len(list)):
        seclarge=list[0:1]
    	print(seclarge)  
for n in seclarge:
	print(n)      


