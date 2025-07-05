import sys
from itertools import combinations

def calculate_team_power(team, graph):
    """팀의 능력치를 계산하는 함수"""
    power = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            power += graph[team[i]][team[j]] + graph[team[j]][team[i]]
    return power

n = int(input())
graph = []
input = sys.stdin.readline

for _ in range(n):
    graph.append(list(map(int, input().split())))

candidates = [i for i in range(n)]
answer = float('inf')

# 모든 가능한 팀 크기에 대해 확인 (1명 ~ n-1명)
for team_size in range(1, n):
    for start_team in combinations(candidates, team_size):
        # 나머지 사람들이 링크팀
        link_team = [i for i in candidates if i not in start_team]
        
        # 각 팀의 능력치 계산
        start_power = calculate_team_power(start_team, graph)
        link_power = calculate_team_power(link_team, graph)
        
        # 능력치 차이의 최솟값 업데이트
        answer = min(answer, abs(start_power - link_power))

print(answer)





# '''
# 어떻게 두개씩 두개의 조합을 얻어 낼 것인가?

# '''
# import sys
# from itertools import combinations
# n=int(input())
# graph=[]
# input=sys.stdin.readline

# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# # 스타트팀 능력치 구하는 함수

# candidates=[i for i in range(n)]
# print("candidates",candidates)
# answer=99999999999999

# for start_t in combinations(candidates,2):
#     link_list = list(set(candidates) - set(start_t))
#     start_weight=graph[start_t[0]][start_t[1]]+graph[start_t[1]][start_t[0]]
#     for link_t in combinations(link_list,2):
#         link_weight=graph[link_t[0]][link_t[1]]+graph[link_t[1]][link_t[0]]
#         answer=min(answer,abs(start_weight-link_weight))
#         print(f"start_t:{start_t}, link_t:{link_t}")
#         print("start_weight", start_weight)
#         print("link_weight",link_weight)

# print(answer)



