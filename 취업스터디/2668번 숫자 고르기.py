import sys
from collections import defaultdict
sys.setrecursionlimit(10**6) # 재귀 제한 늘리기
input=sys.stdin.readline

def dfs(u,visited):
    visited.add(u)
    checked[u]=1
    for v in g[u]:
        print(f"u:{u}, v:{v}")
      
        if v not in visited:
            print("dfs 수행")
            dfs(v,visited.copy())

        else: # 사이클이 생기면 이제 뽑는다
            result.extend(list(visited))
            return
        
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