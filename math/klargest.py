ls=[3,2,4,1,5,6,9]
k=int(input("find kth largest list element"))
if(k>len(ls)):
	print("max limit exceeded")
	exit()
while(k>1):
	print(ls)
	large=max(ls)
	ls.remove(large)
	k-=1
print(max(ls))
