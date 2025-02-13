# 1. 본인꺼로 돌아오면 가능한 조합
# 2. 본인 자시느올 돌아오는거 있으면 무조건 먼저 추가 후 visit
import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 늘리기
n=int(input())
graph=[0]*(n+1) # 리스트 안에 리스트는 굳이 필요가 없다 하나만 오면 되니깐

# 그래프로 입력 받기
for i in range(1,n+1):
    graph[i]=int(input())

visited=[False]*(n+1)
finished=[False]*(n+1) # 탐색이 완전히 종료된 노드(즉 정답 경로를 찾은 노드들)
answer=[]

def dfs(current):
    # 초반에 바로 한번 정리해주는게 필요하다-> 자기자신으로 돌아올 수 있는게 있는지
    if visited[current]: # 일단 한번이라도 방문한 이력이 있다. -> 즉 스택이 쌓여 경로를 찾고 있는 와중에 노드
        if not finished[current]: # 방문했지만 아직 탐색이 끝나지 않은 노드 = 순환 발견
            # (3) 이 시점에서는 '확실히' 순환이 존재합니다!
            temp=current
            while True:
                answer.append(temp)
                temp=graph[temp] # 이 노드와 연관된 노드는 어떻게 되나? # graph[temp]와 temp를 두면서 연쇄적으로 찾는다. 
                if temp==current: # 그 연관된 끝에 시작점과 일치하면
                    break     
        
        
        return
    

    visited[current]=True # 일단 시작하면 방문노드 True로 바꿔준다.
    dfs(graph[current]) # 그 다음 현재노드와 연결되어 있는 2층 노드 바로 dfs 실행
    finished[current]=True # 정답으로 인정되든 완전 아닌 경우든 경로 탐색에 있어서 이제 배제 시킬 노드
 


# 모든 노드에 대해 순환 확인
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

# 정답 정렬 후 출력
answer.sort()
print(len(answer))
for num in answer:
    print(num)

# 예시: 1 → 2 → 3 → 1 의 순환이 있다고 가정

# 1. dfs(1) 호출
#    - visited[1] = True
#    - dfs(2) 호출

# 2. dfs(2) 호출
#    - visited[2] = True
#    - dfs(3) 호출

# 3. dfs(3) 호출
#    - visited[3] = True
#    - dfs(1) 호출

# 4. 다시 dfs(1) 호출될 때:
#    - visited[1]이 True이고
#    - finished[1]이 False인 상태
#    - 이 시점에서 1→2→3→1 순환이 '확실히' 존재!