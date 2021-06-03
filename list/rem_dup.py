dict = {}
duplicates=[]

def remove_dup(arr):
    for x in arr:
        if x not in dict:
            dict[x]=0
        dict[x]+=1
    res = []
    for x,c in dict.items():
        res.append(x)
    return res


print(remove_dup([1,1,2,1,2,4,0,4]))
