n, k = map(int, input().split())
num_list = list(map(int, input().split()))

left = 0
max_length = 0
count_dict = {}

for right in range(n):
    # 현재 원소를 윈도우에 추가
    if num_list[right] not in count_dict:
        count_dict[num_list[right]] = 1
    else:
        count_dict[num_list[right]] += 1
    
    # 현재 원소의 개수가 k를 초과하면 left 포인터를 이동
    while count_dict[num_list[right]] > k:
        count_dict[num_list[left]] -= 1
        if count_dict[num_list[left]] == 0:
            del count_dict[num_list[left]]
        left += 1
    
    # 현재 윈도우 크기로 최대값 갱신
    max_length = max(max_length, right - left + 1)

print(max_length)