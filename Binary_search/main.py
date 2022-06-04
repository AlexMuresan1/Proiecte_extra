import numpy as np

def binary_search(l,x):
    s=0
    e=len(LIST)-1
    while s<=e:
        mid=(s+e)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            e=mid-1
        elif l[mid]<x:
            s=mid+1
    return -1

LIST=np.random.randint(0,100,50)
LIST.sort()
x=np.random.randint(0,100,1)
result=binary_search(LIST,x)

if result !=-1:
    print("The element is at position",result)
else:
    print("The element was not in the list")


