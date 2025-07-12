import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n,m=map(int,input().split())

graph=[[]*n for _ in range(n)]

count=0


arrive = False

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start,depth):
    global arrive
    visited[start]=True
    '''
    if 문을 통해 어떻게 완전히 연결되었다는 것을 알 수 있을까?
    아니면 반환의 조건은 무엇인가?
    '''
    if depth==5:
        arrive=True
        return 
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i,depth+1)
    visited[start]=False
         


for i in range(n):
    visited=[False]*n
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)


        







