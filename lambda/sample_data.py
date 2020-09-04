lst=[x for x in range(1,10)]
sqr=list(map(lambda x:x**2,lst))
print(max(sqr)-min(sqr))
