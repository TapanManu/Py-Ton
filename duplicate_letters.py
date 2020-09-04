str=input('get the string')
ls=[x for x in str]
dup=list(set(ls))
if len(dup)==len(ls):
	print("string has unique letters only")
else:
	print("string has repetitions")
