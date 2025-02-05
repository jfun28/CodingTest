import sys
INF=sys.maxsize
n=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a][b]=1
    graph[b][a]=1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k]+graph[k][b]:
                graph[a][b]=graph[a][k]+graph[k][b]

print(graph)

cm, cm_score = [], INF
for i in range(1, n+1):
    score = 0
    for j in range(1, n+1):
        score = max(score, graph[i][j])
    if score < cm_score:
        cm = []
        cm_score = score
    elif score == cm_score:
        cm.append(i)
 
print(cm_score, len(cm))
print(*cm)
    
# print(*cm)  # 출력: 1 2 3
# print(cm)   # 출력: [1, 2, 3]
