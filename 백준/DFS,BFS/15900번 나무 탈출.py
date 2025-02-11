import sys
sys.setrecursionlimit(1 << 30)
input=sys.stdin.readline
n=int(input())

# 트리저장
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# 해당 노드까지의 깊이를 저장함
arr=[0]*(n+1)
print("graph",graph)

def dfs(cur,prv,cnt):
    # 해당 노드의 깊이
    arr[cnt]=cnt
    for nxt in graph[cur]:
        if nxt==prv: # 만약 방문한 노드가 직전에 노드라면은 건너띈다.
            continue
        dfs(nxt,cur,cnt+1)
dfs(1,0,0)

cnt=0
# 리프노드의 깊이들을 더해준다
for i in range(2,n+1):
    if len(graph[i])==1: # 자기 위에 부모 노드 하나 밖에 없을 것이다. 
        cnt+=arr[i]

# 리프노드들의 깊이의 합이 홀수이면 Yes
if cnt%2==1:
    print("Yes")

else:
    print("No")