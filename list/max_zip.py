y=list((1,2,3,4))
z=list((9,8,7,6))
print(max([x[1]-x[0] for x in zip(y,z)]))
