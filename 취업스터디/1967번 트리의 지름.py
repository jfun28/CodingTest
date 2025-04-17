import sys
sys.setrecursionlimit(int(1e6))

n=int(input())
graph=[[] for _ in range(n+1)]

def find_dfs(start,now_weight):
    for b,weight in graph[start]:
        if visited[b]==-1:
            visited[b]=now_weight+weight
            find_dfs(b,visited[b])

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


visited=[-1]*(n+1)
visited[1] = 0 # 루트 노드는 거리가 0으로 초기화
find_dfs(1,0)

max_distance = max(visited) # 최장 거리
max_node = visited.index(max_distance) # 해당 노드


# max_node에서 시작해 각 정점까지의 거리 계산
visited = [-1] * (n+1)
visited[max_node] = 0 
find_dfs(max_node, 0)

print(max(visited)) # 최장 거리(=트리의 지름) 출력