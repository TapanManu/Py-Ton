natural=[n for n in range(1,9)]
sqr=[n**2 for n in natural]
cub=[n**3 for n in natural]

#sum of number+sqr(number)+cube(number) upto range n

print(list(map(lambda x:x[0]+x[1]+x[2],zip(natural,sqr,cub))))
