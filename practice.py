from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 이전 위치를 저장할 2차원 리스트
    path = [[None] * m for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:  # 도착점에 도달했다면
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if graph[nx][ny] == 0:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                path[nx][ny] = (x, y)  # 이전 위치 저장
                queue.append((nx, ny))
    
    # 경로 역추적
    current = (n-1, m-1)  # 도착점부터 시작
    route = []
    
    while current is not None:  # 시작점에 도달할 때까지
        route.append(current)
        current = path[current[0]][current[1]]
    
    return route[::-1]  # 경로를 시작점부터 도착점 순서로 반환

# 경로 출력
path = bfs(0, 0)
print("최단 경로:")
print(f"길이: {len(path)}")
print("경로:", end=" ")
for x, y in path:
    print(f"({x},{y})", end=" ")