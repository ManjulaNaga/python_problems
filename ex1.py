def has_good_subarray(ar, k):
    if len(ar)==0:
        return False
    res = ar[0]
    for i in range(len(ar)-1):
        if res > k:
            i = i+1
            res= ar[i+1]
        else:
            res += ar[i]
        if  res == k:
            return True
    return False

print(has_good_subarray([23, 2, 4, 7],6))

print(has_good_subarray([5, 0, 0, 0],3))

print(has_good_subarray([],1))