import sys
input=sys.stdin.readline

n,s=map(int,input().split())

num_array=list(map(int,input().split()))

count=0

answer=[]

def dfs_search(start):
    global answer,count

    if sum(answer)==s and len(answer)>0:
        count+=1
        

    for i in range(start,n):
        answer.append(num_array[i])
        dfs_search(i+1)
        answer.pop()



dfs_search(0)

print(count)