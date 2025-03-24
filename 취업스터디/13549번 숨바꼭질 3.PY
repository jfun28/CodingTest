import heapq
import sys
INF=int(1e9)
input=sys.stdin.readline
my_num,brother_num=map(int,input().split())
distance=[INF]*100001
def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,current=heapq.heappop(q)
        if distance[current]<dist:
            continue
        for n in (current+1,current-1,current*2):
            if n <0 or n>100000:
                continue
            cost=dist
            if n!=current*2:
                cost=dist+1 #현재의 cost를 과거의 cost인 dist에 1을 더한다

            if cost<distance[n]:
                distance[n]=cost
                heapq.heappush(q,(cost,n))



dijkstra(my_num)

print(distance[brother_num])