n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(input().strip()))

friends=[[0]*n for i in range(n)]
for i in range(n): # 자기 본인
    for j in range(n):
        for k in range(n):
            if k==j: # 본인 자신
                continue

            if graph[j][k]=='Y' or (graph[j][i]=='Y' and graph[i][k]=='Y'):# 나랑 친구이거나 한다리 건너면 아는 사이
                friends[j][k]=1

popular=0
for person in friends:
    popular=max(sum(person),popular)
print(popular)