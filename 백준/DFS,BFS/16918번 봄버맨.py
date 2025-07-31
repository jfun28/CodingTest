'''
1. 폭탄두기
2. 폭탄 터트리기
3. 폭탄 위치 찾기
'''
import sys
input=sys.stdin.readline
from collections import deque
graph=[]
t = 1 
R,C,N=map(int,input().split())

for _ in range(R):
    graph.append(list(input().strip()))


def install_bomb(): # 폭탄 설치하기
    # 2차원 리스트 전체를 순회하지 않고, 한 번에 '.'를 'O'로 바꿔줌
    for i, row in enumerate(graph):
        graph[i] = ['O' if cell == '.' else cell for cell in row]


def pop_bomb(): # 폭탄 터트리기
    while temp:
        x,y=temp.popleft()
        graph[x][y]='.'
        for i in splash:
            nx=x+i[0]
            ny=y+i[1]
            if R>nx>=0 and C>ny>=0 :
                graph[nx][ny]='.'


def find_bomb(): # 폭탄 위치 찾기
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='O':
                temp.append([i,j])

splash=[[1,0],[-1,0],[0,1],[0,-1]]

# if N%2!=0:
#     N-=1
#     while N>0: # 남은 시간 동안
#         temp=deque()
#         find_bomb()
#         install_bomb()
#         N-=1
#         if N==0: # 만약 시간이 N초면
#             break
        
#         pop_bomb()
#         N-=1 # 시간 1초 지나

#     for i in graph:
#         print(*i,sep='')

# else:
#     graph=[['O']*C for _ in range(R)]
#     for i in graph:
#         print(*i,sep='')

temp=deque()
while t<N:
    find_bomb()
    install_bomb()
    t+=1
    if t==N:
        break

    pop_bomb()
    t+=1


for g in graph:
    print(''.join(g))