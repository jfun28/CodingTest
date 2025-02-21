from collections import deque


def solution(numbers, target):

    n=len(numbers)
    cnt=0
    queue=deque()
    queue.append([0,0])

    while queue:
        current_sum,index =queue.popleft()
        
        if index==n:
            if current_sum==target:
                cnt+=1

        else:
            number=numbers[index]
            queue.append([current_sum+number,index+1])
            queue.append([current_sum-number,index+1])

            
    return cnt




















# from collections import deque
# queue=deque()

# def solution(numbers, target):
#     leaves=[0]
#     count=0
#     queue.append(numbers)
#     print("queue",queue)
#     while queue:
#         num=queue.popleft()
#         temp=[]

#         # 자손 노드
#         for leaf in leaves:
#             temp.append(leaf+num)
#             temp.append(leaf-num)

#         leaves=temp

#     for leaf in leaves:
#         if leaf==target:
#             count+=1

#     return count, leaves

# count, leaves=solution([1, 1, 1, 1, 1], 3)

# print("leaves", leaves)
# print("count", count)


from collections import deque
def solution(numbers, target):
        
    n = len(numbers)
    count = 0
    queue = deque([(0, 0)])  # (현재까지의 합계, 현재 인덱스)
    
    while queue:
        current_sum, index = queue.popleft()
        
        if index == n:  # 모든 숫자를 다 사용했을 때
            if current_sum == target:  # 타겟 넘버와 일치하면
                count += 1
        else:
            # 현재 숫자를 더하거나 빼는 두 가지 경우를 큐에 추가
            number = numbers[index]
            queue.append((current_sum + number, index + 1))
            queue.append((current_sum - number, index + 1))
            
    return count