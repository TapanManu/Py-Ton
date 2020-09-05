start=ord('a')
end = ord('z')
wordmap={}
for i,j in zip(range(start,end+1),range(1,27)):
	wordmap[chr(i)]=j
print(wordmap)
