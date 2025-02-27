import sys
input=sys.stdin.readline
from itertools import combinations

n,m=map(int,input().split())

graph=[]

house=[]
chicken=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))



for y in range(n):
    for x in range(n):
        if graph[y][x]==1:
            house.append((x,y))

        elif graph[y][x]==2:
            chicken.append((x,y))

result=2*n*len(house)

for comb in list(combinations(chicken,m)):
    dist=0
    for x,y in house: # 해당 집에서 가장 가까운 치킨집 까지 거리 찾기
        temp=2*n*len(house)
        for i,j in comb: # 현재 가지고 있는 세개의 조합으로 해보기
            temp=min(temp,abs(x-i)+abs(y-j))
        dist+=temp # 현재 

    result=min(result,dist) # 현재 세개의 조합에서 가장 작으면 업데이트







































# import sys
# input=sys.stdin.readline
# from itertools import combinations 

# n,m=map(int,input().split())

# graph=[]
# house=[]
# chicken=[]

# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# for y in range(n):
#     for x in range(n):
#         if graph[y][x]==1:
#             house.append((x,y))
#         elif graph[y][x]==2:
#             chicken.append((x,y))
            

# result=n*2*len(house) # 치킨집과 집과의 거리 가장 거리가 멀때 상한값 설정(distance 때 무한으로 설정하는 것과 같음)


# for comb in list(combinations(chicken,m)): # 가장 가까운 치킨집에서 몇개를 조합해서 선택해야하는지 
#     dist=0
#     for i,j in house:
#         temp=n*2
#         for x, y in comb:
#             temp=min(temp,abs(x- i)+abs(y -j))
#         dist+=temp
        
#     result=min(result,dist)
    
# print(result)
        