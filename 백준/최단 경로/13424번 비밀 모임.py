import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def disjkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
                

t=int(input())
for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    total_dis=[0]*(n+1)
    
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    k=int(input())
    room=list(map(int,input().split()))
    for i in range(k):       
        distance=[INF]*(n+1)
        disjkstra(room[i])
        for j in range(1,n+1):
            total_dis[j] += distance[j]

    min_index=0
    noww=INF
    for i in range(1,n+1):
        if noww>total_dis[i]:
            noww=total_dis[i]
            min_index=i
            
    print(min_index)