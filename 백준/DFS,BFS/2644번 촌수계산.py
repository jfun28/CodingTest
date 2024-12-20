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
    if v==b:
        return count  

    count+=1
    visited[v]=True

    for i in graph[v]: # a 시작해서 b를 만나면 끝난다
        if visited[i]==False:
            result = dfs(i, count)
         
            if result != -1:  # 목적지를 찾은 경우
                return result

    return -1

result=dfs(a,count)
print(result)
