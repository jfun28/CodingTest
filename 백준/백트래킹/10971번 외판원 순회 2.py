n=int(input())
costs=[list(map(int,input().split())) for _ in range(n)]
# 최소 비용
min_cost=int(1e9)


def search(start,next,cost,visited): # start: 처음 시작한 도시이자 마지막으로 돌아갈 곳, next: 현재 위치한 도시, cost: 현재까지의 누적 비용, visited: 방문한 도시들
    global min_cost

    # 모든 도시 순회를 하였는지 확인
    if False not in visited:
        # 마지막 도시에서 다시 출발지로 올 수 있는지 확인
        print(f'next: {next}, start: {start}')
        if costs[next][start]>0:
            min_cost=min(min_cost,cost+costs[next][start])
        return min_cost

    # 시작점으로 부터 모든 도시를 순회   
    for i in range(n):
        # 도시끼리 연결되었는지, 이미 방문한 도시인지, 현재 비용이 최소 비용보다 큰지 확인
        if (costs[next][i]>0) and (visited[i]==False) and (cost< min_cost):
            print(f'start:{start}, next: {next}, i:{i}')
            visited[i]=True
            search(start,i,cost+costs[next][i],visited)
            visited[i]=False

# 출발지가 정해져 있지 않아 모든 도시로 시작하는 방법을 모두 순회

for i in range(n): # i번 도시에서 시작해서, 현재 i번 도시에 있고, 비용은 0이다"라는 의미
    visited=[False]*n
    visited[i]=True
    search(i,i,0,visited)


print(min_cost)
