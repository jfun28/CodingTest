import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 늘리기

n = int(input())
graph = [0] * (n+1)  # 리스트 안에 리스트가 필요없으므로 단순화

# 그래프 입력 받기
for i in range(1, n+1):
    graph[i] = int(input())

visited = [False] * (n+1)
finished = [False] * (n+1)  # 탐색이 완전히 종료된 노드 체크
answer = []

def dfs(current):
    if visited[current]:
        if not finished[current]:  # 방문했지만 아직 탐색이 끝나지 않은 노드 = 순환 발견
            temp = current
            while True:
                answer.append(temp)
                temp = graph[temp]
                if temp == current:
                    break
        return
    
    visited[current] = True
    dfs(graph[current])
    finished[current] = True  # 탐색 완료 표시

# 모든 노드에 대해 순환 확인
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

# 정답 정렬 후 출력
answer.sort()
print(len(answer))
for num in answer:
    print(num)