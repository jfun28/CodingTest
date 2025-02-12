import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)


def dfs(cur):
    if visited[cur] or cur in is_fan: # is_fan이 이렇게 하면은 key값만 반복적으로 호출되서 나온다. 
        return
    visited[cur]=True

    if not graph[cur]:
        print("yes")
        exit()

    for next in graph[cur]:
        if next not in is_fan and not visited[next]: 
            
            dfs(next)
            visited[next]=False # 추후에 옆으로 나와 다른 경로 탐색하기 위해서(백트래킹킹)

fan_num=int(input())
is_fan={}
fan_list=list(map(int,input().split()))

for fan in fan_list:
    is_fan[fan]=True

dfs(1)
print("Yes")





# import sys
# sys.setrecursionlimit(10**5)
# input=sys.stdin.readline
# n,m=map(int,input().split())

# graph=[[0]*(m+1) for _ in range(n+1)]
# for _ in range(m):
#     a,b=map(int,input().split())
#     graph[a][b]=1

# visited=[False]*(n+1)
# fan_num=int(input())
# fan_list=[0]*(n+1)

# fan=list(map(int,input().split()))
# for i in fan:
#     fan_list[i]=1
# global count
# def dfs(v):
#     global count
#     visited[v]=True
#     print(v,end=' ')
#     for i in range(1,n+1):
#         if visited[i]==False and graph[v][i]==1:
#             if fan_list[i]==1:
#                 count+=1
#             dfs(i)
#     return count

# count=dfs(1)
# print(count)
# print("Yes" if not count == 0 else "yes")

