n,s=map(int,input().split())

n_list=list(map(int,input().split()))

cnt=0

ans=[]

def dfs_search(start):
    global cnt
    if sum(ans)==s and len(ans)>0:
        cnt+=1
    

    for i in range(start,n):
        ans.append(n_list[i])
        dfs_search(i+1)
        ans.pop()

    return cnt

result=dfs_search(0)

 

print(result)