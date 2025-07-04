import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

vertices=[[0] for _ in range(n+1)]
parent=[0]*(n+1)


for _ in range(n-1):
    a,b=map(int,input().split())
    vertices[a].append(b)
    vertices[b].append(a)


parent[1]=0

q=deque()

q.append(1)

while q:
    current=q.popleft() # bfs로 위의 노드가 있는 거 끼리 훑으면은 parent 노드 찾기 좋다
    for v in vertices[current]:
        if parent[v]==0:
            parent[v]=current
            q.append(v)

for i in parent[2:]:
    print(i)






























# import sys
# from collections import deque
# input=sys.stdin.readline

# n=int(input())

# vertices=[[0] for _ in range(n+1)]
# parent=[0]*(n+1)

# for _ in range(n-1):
#     a,b=map(int,input().split())
#     # 두 정점의 linked_list에 저장
#     vertices[a].append(b)
#     vertices[b].append(a)

# parent=[0]*(n+1) # 각 노드들의 부모를 기록하는 배열

# parent[1]=0
# q=deque()
# q.append(1)

# while q:
#     current=q.popleft()
#     for v in vertices[current]:
#         if parent[v]==0:
#             parent[v]=current
#             q.append(v)

# print("vertices", vertices)
# print("parent",parent)
# print('\n'.join(map(str,parent[2:])))

