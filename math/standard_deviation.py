def std(*num):
	mean=sum(num)/len(num)
	variance=[(x-mean)**2 for x in num]
	var = sum(variance)/len(num)
	return var ** 0.5

print(std(1,2,3,4,5))
