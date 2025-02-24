# 다익스트라 알고리즘
import heapq
import sys
INF=sys.maxsize

n=int(input())

bus=int(input())
graph=[[] for i in range(n+1)]
 
distance=[INF]*(n+1)

for _ in range(bus):
    start,end,cost=map(int,input().split())
    graph[start].append((end,cost))

start_city,end_city=map(int,input().split())

def find_path(start):
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cost, current_node=heapq.heappop(q)
        if distance[current_node]<cost:
            continue
        for i in graph[current_node]:
            new_cost=cost+i[1]
            next_node=i[0]
            if new_cost<distance[next_node]:
                distance[next_node]=new_cost
                heapq.heappush(q,(new_cost,next_node))


find_path(start_city)

print(distance[end_city])