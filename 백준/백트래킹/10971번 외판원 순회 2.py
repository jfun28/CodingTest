n=int(input())
graph=[]
min_weight=[]
min_cost=int(1e9)

for _ in range(n):
    graph.append(list(map(int,input().split())))


def dfs_search(start,next,cost,visited):
    global min_cost
    
    # 모든 도시 순회를 하였는지 확인
    if False not in visited:
        # 마지막 도시에서 다시 출발지로 올 수 있는지 확인
        if graph[next][start]>0:
            min_cost=min(min_cost,cost+graph[next][start])
        return min_cost
    
    # 시작점으로부터 모든 도시 순회
    for i in range(n):
        if (graph[next][i]>0) and (visited[i]==False) and (cost<min_cost):
            visited[i]=True
            dfs_search(start,i,cost+graph[next][i],visited)
            visited[i]=False
           

for i in range(n):
    visited=[False]*n
    visited[i]=True
    dfs_search(i,i,0,visited)



print(min_cost)
























# n = int(input())

# graph = []
# min_cost = int(1e9)
# call_count = 0  # 함수 호출 횟수 추적
# best_path = []  # 최적 경로 추적

# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# print("=== 그래프 정보 ===")
# print(f"도시 수: {n}")
# print("인접 행렬:")
# for i in range(n):
#     print(f"  {graph[i]}")
# print()

# def search(start, next, cost, visited, path, depth=0):
#     global min_cost, call_count, best_path
    
#     call_count += 1
#     indent = "  " * depth  # 들여쓰기로 깊이 표현
    
#     print(f"{indent}[호출 {call_count}] 현재 위치: {next}, 비용: {cost}")
#     print(f"{indent}  경로: {' -> '.join(map(str, path))}")
#     print(f"{indent}  방문 상태: {visited}")
    
#     # 가지치기 조건 확인
#     if cost >= min_cost:
#         print(f"{indent}  ❌ 가지치기: 현재 비용({cost}) >= 최소 비용({min_cost})")
#         return min_cost
    
#     # 모든 도시 순회를 하였는지 확인
#     if False not in visited:
#         print(f"{indent}  ✅ 모든 도시 방문 완료!")
#         # 마지막 도시에서 다시 출발지로 올 수 있는지 확인
#         if graph[next][start] > 0:
#             total_cost = cost + graph[next][start]
#             final_path = path + [start]
#             print(f"{indent}  🔄 출발지로 복귀 가능: {next} -> {start} (비용: {graph[next][start]})")
#             print(f"{indent}  📍 완성된 경로: {' -> '.join(map(str, final_path))}")
#             print(f"{indent}  💰 총 비용: {total_cost}")
            
#             if total_cost < min_cost:
#                 min_cost = total_cost
#                 best_path = final_path.copy()
#                 print(f"{indent}  🎉 새로운 최적 경로 발견! 최소 비용: {min_cost}")
#                 print(f"{indent}  🏆 최적 경로: {' -> '.join(map(str, best_path))}")
#             else:
#                 print(f"{indent}  ⚠️  현재 경로가 최적이 아님")
#         else:
#             print(f"{indent}  ❌ 출발지로 복귀 불가능: {next} -> {start}")
#         return min_cost
    
#     print(f"{indent}  🔍 다음 도시 탐색...")
    
#     # 다음 도시 탐색
#     for i in range(n):
#         if (visited[i] == False) and (graph[next][i] > 0) and (cost < min_cost):
#             print(f"{indent}    🚀 {next} -> {i} 탐색 시작 (비용: {graph[next][i]})")
#             visited[i] = True
#             new_path = path + [i]
#             search(start, i, cost + graph[next][i], visited, new_path, depth + 1)
#             visited[i] = False
#             print(f"{indent}    ⬅️  {next} -> {i} 탐색 완료 (백트래킹)")
#         elif visited[i] == True:
#             print(f"{indent}    ⏭️  도시 {i} 이미 방문함")
#         elif graph[next][i] <= 0:
#             print(f"{indent}    🚫 도시 {i}로 갈 수 없음 (비용: {graph[next][i]})")
#         elif cost >= min_cost:
#             print(f"{indent}    ✂️  도시 {i} 가지치기 (현재 비용이 최소 비용 이상)")

# print("=== TSP 탐색 시작 ===")
# for i in range(n):
#     print(f"\n🏁 출발 도시: {i}")
#     visited = [False] * n
#     visited[i] = True
#     search(i, i, 0, visited, [i])
#     print(f"출발 도시 {i} 탐색 완료\n" + "="*50)

# print("\n=== 최종 결과 ===")
# print(f"🎯 최소 비용: {min_cost}")
# print(f"🏆 최적 경로: {' -> '.join(map(str, best_path))}")
# print(f"📊 총 함수 호출 횟수: {call_count}")

# if min_cost == int(1e9):
#     print("❌ 모든 도시를 방문하는 경로가 존재하지 않습니다.")
# else:
#     print(min_cost)