def solution(arrs,M):
    # 초기 설정 변수
    left=0
    right=max(arrs)-min(arrs)
        
    answer=right
    
    while left<=right:
        mid=(left+right)//2
        
        if can_divide(arrs,M,mid):
            answer = mid  # 가능하다면 현재 값을 답으로 저장
            right = mid - 1  # 더 작은 값도 가능한지 확인
    
        else:
            left=mid+1
            
        
    return answer


def can_divide(arrs,M,max_score):
    '''
    배열을 M개 이하의 구간으로, 각 구간의 점수가 max_score 이하가 되도록 나눌 수 있는지 확인
    '''
    count=1
    min_val = max_val = arrs[0]  # 현재 구간의 최솟값과 최댓값

    for i in range(1,len(arrs)):
        current_min=min(min_val,arrs[i])
        current_max=max(max_val,arrs[i])
        
        # 현재 값을 포함시켰을 때 점수가 max_score를 초과하면 새 구간 시작
        if (current_max-current_min) > max_score:
            count+=1
            min_val = max_val = arrs[i] # 다시 구간 분할에서 맨 처음 오는 구간
        
        else:
            min_val=current_min
            max_val=current_max
                     
        
        if count>M:
            return False 
        
        
    return True
     

n,m=map(int,input().split())
arrs=list(map(int,input().split()))
print(solution(arrs,m))   
    







# # 1. abs를 써야한다
# # 2. 어떻게 모든 경우의 수를 나눌 수가 있을까 M개 이하로 나누는 것이지 M개로 나누는 것이 아니다.
# # 3. 이진 탐색?
# def solution(arr, M):
#     # 가능한 점수의 최솟값과 최댓값 설정
#     left = 0
#     right = max(arr) - min(arr)
    
#     answer = right  # 최악의 경우 답은 배열 전체의 점수
    
#     while left <= right:
#         mid = (left + right) // 2  # 현재 테스트할 점수 기준값
        
#         # mid 값을 기준으로 배열을 나눌 수 있는지 확인
#         if can_divide(arr, M, mid):
#             answer = mid  # 가능하다면 현재 값을 답으로 저장
#             right = mid - 1  # 더 작은 값도 가능한지 확인
#         else:
#             left = mid + 1  # 불가능하다면 더 큰 값을 확인
    
#     return answer

# def can_divide(arr, M, max_score):
#     """
#     배열을 M개 이하의 구간으로, 각 구간의 점수가 max_score 이하가 되도록 나눌 수 있는지 확인
#     """
#     count = 1  # 구간의 개수 (첫 번째 구간은 무조건 시작)
#     min_val = max_val = arr[0]  # 현재 구간의 최솟값과 최댓값
    
#     for i in range(1, len(arr)):
#         # 현재 값을 구간에 포함시킬 경우 점수 계산
#         curr_min = min(min_val, arr[i])
#         curr_max = max(max_val, arr[i])
        
#         # 현재 값을 포함시켰을 때 점수가 max_score를 초과하면 새 구간 시작
#         if curr_max - curr_min > max_score:
#             count += 1
#             min_val = max_val = arr[i]
#         else:
#             min_val = curr_min
#             max_val = curr_max
        
#         # 필요한 구간의 수가 M을 초과하면 불가능
#         if count > M:
#             return False
    
#     return True  # M개 이하의 구간으로 나눌 수 있음

# # 입력 처리
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# # 결과 출력
# print(solution(arr, M))