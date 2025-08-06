n,s=map(int,input().split())

array=list(map(int,input().split()))
cnt=0
ans=[]

def search(start):
    global cnt
    if sum(ans)==s and len(ans)>0:
        cnt+=1

    for i in range(start,n):
        ans.append(array[i])
        search(i+1)
        ans.pop()


search(0)
print(cnt)


