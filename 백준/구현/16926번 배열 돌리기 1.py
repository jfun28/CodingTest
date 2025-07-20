import sys
from collections import deque
input=sys.stdin.readline

N, M ,R= map(int,input().split())
graph=[]
answer = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(input().split()))

num=min(N,M)//2

deq=deque()

for i in range(num):
    
    deq.clear()
    # 위쪽
    deq.extend(graph[i][i:M-i])

    # 오른쪽
    deq.extend([row[M-i-1] for row in graph[i+1:N-i-1]]) # Matrix 일단 중간공간 확보

    # 아래쪽
    deq.extend(graph[N-i-1][i:M-i][::-1]) 

    # 왼쪽
    deq.extend(row[i] for row in graph[i+1:N-i-1][::-1]) 

    deq.rotate(-R)

    for j in range(i,M-i):  # 위쪽
        answer[i][j]=deq.popleft()

    for j in range(i+1,N-i-1): # 오른쪽
        answer[j][M-i-1]= deq.popleft()

    for j in range(M-i-1,i-1,-1): # 아래쪽
        answer[N-i-1][j]=deq.popleft()

    for j in range(N-i-2,i,-1): # 왼쪽
        answer[j][i]=deq.popleft()


for line in answer:
    print(" ".join(line))















