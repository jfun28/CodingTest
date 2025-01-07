def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif target<=array[mid]:
            end=mid-1
        else:
            start=mid+1
    return None
    

n=int(input())
array=list(map(int,input().split()))

m=int(input())
array2=list(map(int,input().split()))

array.sort()

for i in array2:
    if binary_search(array,i,0,len(array)-1)!=None:
        print(1)
    else:
        print(0)