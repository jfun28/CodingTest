n, m = map(int, input().split())

listen_list = []
see_list = []
result = {}

for _ in range(n):
    listen_list.append(input())

for _ in range(m):
    see_list.append(input())

listen_list.sort()
see_list.sort()

# 더 긴 리스트를 기준으로 딕셔너리 생성
if len(listen_list) >= len(see_list):
    for i in listen_list:
        result[i] = 1
    
    for j in see_list:
        if j in result:
            result[j] += 1
else:
    for i in see_list:
        result[i] = 1
    
    for j in listen_list:
        if j in result:
            result[j] += 1

final_result = []
for k in result:
    if result[k] >= 2:
        final_result.append(k)

final_result.sort()  # 정렬된 결과 출력을 위해 추가

print(len(final_result))
for name in final_result:
    print(name)