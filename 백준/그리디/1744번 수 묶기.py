# from collections import deque
# n=int(input())
# num_list=[]
#
# for _ in range(n):
#     num=int(input())
#     num_list.append(num)
#
# num_list.sort(reverse=True)
# answer=0
# sum_answer=0
# num_list = deque(num_list)
# while len(num_list)>0:
#     if len(num_list)>=2:
#         one=num_list.popleft()
#         two=num_list.popleft()
#         if one>1 and two>1:
#             answer=one*two
#             sum_answer+=answer
#
#         elif 0<one<=1 and 0<two<=1:
#             answer = one + two
#             sum_answer += answer
#
#         elif one <= 0 and two <= 0:
#             answer = one * two
#             sum_answer += answer
#
#         else:
#             if one>0:
#                 num_list.appendleft(two)
#                 sum_answer+=one
#
#             else:
#                 num_list.appendleft(one)
#                 sum_answer += two
#
#
#     else:
#         one = num_list.popleft()
#         sum_answer+=one
#
# print(sum_answer)
#


n = int(input())
nums = [int(input()) for _ in range(n)]

pos = []  # 1보다 큰 양수
ones = [] # 1
neg = []  # 음수
zeros = [] # 0

for num in nums:
    if num > 1: pos.append(num)
    elif num == 1: ones.append(num)
    elif num == 0: zeros.append(num)
    else: neg.append(num)

pos.sort(reverse=True)
neg.sort()

result = sum(ones)  # 1은 곱하는 것보다 더하는 게 이득

# 양수 처리
for i in range(0, len(pos)-1, 2):
    result += pos[i] * pos[i+1]
if len(pos) % 2:
    result += pos[-1]

# 음수 처리
for i in range(0, len(neg)-1, 2):
    result += neg[i] * neg[i+1]
if len(neg) % 2 and not zeros:  # 남은 음수가 있고 0이 없으면 더함
    result += neg[-1]

print(result)