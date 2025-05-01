import sys

input = sys.stdin.readline
N = int(input())                                # 돌의 개수
A = [0] + list(map(int, input().split()))       # 돌의 수 Ai

def solution(start, end): # 이분 탐색의 시작점(최소 k값), 이분 탐색의 시작점(최대 k값)
    answer = 0

    while start <= end: # 최악과 최소 중 가장 적합한 상한 힘의 크기를 구하다
        mid = (start + end) // 2 # mid가 상한값

        visited = [False] * (N+1) # 각돌에 방문했는지 여부를 체크
        flag = False # 마지막 돌에 방문할수 있다면 True 없으면 False

        stack = [1] # 깊이우선 탐색을 위한 스택
        visited[1] = True # 첫번째 스톤 각돌에 방문

        while stack:
            now = stack.pop()
            if now == N:
                flag = True
                break
            for idx in range(now+1, N+1): #현재 위치(now)에서 오른쪽에 있는 모든 돌들을 확인한다
                temp = (idx - now) * (1 + abs(A[now] - A[idx])) # 현재 위치(now)에서 다음 위치(idx)로 점프하는 데 필요한 힘을 계산합니다.
                if temp <= mid and not visited[idx]:  #계산된 힘(temp)이 현재 이분 탐색에서 설정한 최대 힘(mid)보다 작거나 같은지 확인
                    # 또한 다음 위치(idx)에 아직 방문하지 않았는지도 확인합니다.
                    # 두 조건이 모두 만족되면, 해당 돌로 점프할 수 있습니다.
                    stack.append(idx) #점프 가능한 돌의 인덱스를 스택에 추가합니다.
                    visited[idx] = True #해당 돌을 방문했다고 표시합니다(중복 방문 방지).

        if flag: # 도달한다면 더 작은 상한값도 가능한지 체크
            answer = mid
            end = mid - 1
        else: # 도달하지 못하다면 상한값을 좀더 높여서 체크
            start = mid + 1

    return answer

print(solution(1, (N-1) * (1 + abs(A[N] - A[1])))) # 최소 경우 가능한 힘, # 최악의 경우 가능한 힘
