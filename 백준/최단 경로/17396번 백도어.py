import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize # int(1e9) 대신 이걸로 안써서 틀림. 엄청 큰 경우의 수에서는 max.size로 넉넉하게 INF를 설정해줘야겠다. 

n,m=map(int,input().split())
distance=[INF]*(n)
nexus=list(map(int,input().split()))
nexus[-1] = 0
graph=[[] for i in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def find_path(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            next_node=i[0]
            if cost<distance[i[0]] and nexus[next_node]==0:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
            


find_path(0)
print(distance[n-1] if distance[n-1] != INF else -1)