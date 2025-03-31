import sys
input=sys.stdin.readline
n=int(input().strip())

nums=[0 for _ in range(n+1)]
for i in range(1,n+1):
    nums[i]=int(input().strip())

visited=[False for _ in range(n+1)]
paths=[]

def dfs(start,visited,path):
    if visited[start]:
        # 방문한 노드일 경우 사이클 여부 확인
        if start in path: # 현재 노드가 path안에 있으면 사이클이 형성 되었다는 것
            paths.extend(path[path.index(start):])        
        return
    
    visited[start]=True # 방문처리
    path.append(start) # path에 현재 노드 추가

    # 다음 노드로 부터 다시 탐색
    dfs(nums[start],visited,path)



'''
예를 들어, 경로가 [1, 3, 4, 7, 6, 3]인 경우, 노드 3이 반복됩니다:

start는 3입니다 (두 번째 등장한 3)
path.index(start)는 1입니다 (첫 번째 3의 인덱스)
path[path.index(start):]는 [3, 4, 7, 6, 3]입니다 (첫 번째 3부터 끝까지)
이 노드 리스트가 paths에 추가됩니다

'''

for i in range(1, n + 1):
    if not visited[i]:
        # 방문한 경우에만 탐색
        dfs(i, visited, [])

print(len(paths))
for path in sorted(paths):
    print(path)


""" 이문제는 어딘가에 싸이클이 생길수 밖에 없고 한 지점에 두개가 인풋으로 받을 수 없어서 이렇게 하면 풀린다"""


import sys
from collections import defaultdict
sys.setrecursionlimit(10**6) # 재귀 제한 늘리기
input=sys.stdin.readline

def dfs(u,visited):
    visited.add(u)
    checked[u]=1 # 전역변수로 전체 경로에 대해 모니터링한다다
    for v in g[u]: # 현재 시작점으로 부터 연결되어 있는 노드를 하나씩 꺼내본다다
        print(f"u:{u}, v:{v}")
      
        if v not in visited: # 현재 노드에서 확인하는 과정에서 처음 연결된거면 # 받는 거는 무조건 하나의 경우만 존재한다다
            print("dfs 수행")
            dfs(v,visited.copy()) # 또 연결된게 없는지 dfs로 확인

        else: # 사이클이 생기면 이제 뽑는다
            result.extend(list(visited))
            return
        
    

n=int(input().strip())
g=defaultdict(list) # values 값을 리스트로 초기화 시켜준다
for i in range(1, n+1):
    v = int(sys.stdin.readline().strip())
    g[v].append(i)

checked=[0 for _ in range(n+1)]

result=[]

for i in range(1,n+1):
    if not checked[i]:
        dfs(i,set([]))

result.sort()
print(len(result))

for x in result:
    print(x)