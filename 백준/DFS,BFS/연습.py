from collections import deque
# BFS 매서드 정의 
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque([start])

    # 방문한 노드 처리
    visited[start]=True
    while queue:
        # 큐에서 원소 하나하나 popleft로 꺼낸다.
        v=queue.popleft()
        print(v, end=" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9

bfs(graph,1,visited)