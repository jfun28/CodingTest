
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        
        if array[mid]==target:
            return mid
        
        elif array[mid]>=target:
            end=end-1
        
        else:
            start=start+1


    return None




n=int(input())

array=list(map(int,input().split()))

array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m=int(input())
array2=list(map(int,input().split()))

for i in range(m):
    if binary_search(array, array2[i],0, len(array))!=None:
        print("yes",end=' ')
    else:
        print("no",end=' ')

