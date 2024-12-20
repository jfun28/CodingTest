num=int(input())

a,b=map(int,input().split())

n=int(input())
result = []
graph=[[] for _ in range(num+1)]

for _ in range(n):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

visited=[False]*(num+1)

count=0
def dfs(v,count):
    count+=1
    visited[v]=True

    if v==b:
        return count

    for i in graph[v]: # a 시작해서 b를 만나면 끝난다
        if visited[i]==False:
            dfs(i,count)

    return -1

result=dfs(a,count)
print(result)
print("count", count)