def filecount(filename):
	with open(filename,'r') as f:
		arr = [len(line.split(" ")) for line in f.readlines()]
	return sum(arr)

print(filecount("Documents/abstract.txt"))

