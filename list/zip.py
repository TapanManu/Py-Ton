numbers=[(1,2,3),(4,5,6),(7,8,9)]
print(list(zip(*numbers)))

#almost equivalent operation

first=[x[0] for x in numbers]
second = [x[1] for x in numbers]
third = [x[2] for x in numbers]

print(first,second,third)
