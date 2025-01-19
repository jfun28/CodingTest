n,m=map(int,input().split())

n_list=[]
m_list=[]

for _ in range(n):
    n_list.append(input())

for _ in range(m):
    m_list.append(input())

n_list.sort()

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid][:len(target)]==target:
            return mid
        elif target<=array[mid]:
            end=mid-1
        else:
            start=mid+1
    return None
    

count=0

for word in m_list:
    if binary_search(n_list,word,0,n-1)!=None:
        count+=1
    else:
        pass

print(count)