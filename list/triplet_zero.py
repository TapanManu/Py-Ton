def triplet_zero(arr):
    res = []
    arr.sort()
    # Input: [-3, 0, 1, 2, -1, 1, -2]
    for i in range(len(arr)):
        x = arr[i]
        left = i+1
        right = len(arr)-1
        while left < right:
            
            target = arr[left] + x + arr[right]
            #print(arr[left],x,arr[right])
            if target == 0:
                temp = []
                temp.extend([arr[left],x,arr[right]])
                res.append(temp)
                left+=1
                right-=1
            elif target < 0:
                left+=1
            else:
                right-=1
    return res


print(triplet_zero([-5, 2, -1, -2, 3]))
