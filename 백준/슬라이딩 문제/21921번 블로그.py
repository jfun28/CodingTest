# import sys
# input=sys.stdin.readline

# n,x=map(int,input().split())
# visit_list=list(map(int,input().split()))
# answer=0
# answer_list=[0]

# for i in range(n):
#     temp=sum(visit_list[i:i+x])
#     if temp==0:
#         continue
    
#     if answer<=temp:
#         answer=temp
#         answer_list.append(answer)

#     # 여러 개가 최대값일 때는 어떻게 담을 것인가?

# if max(answer_list)!=0:
#     print(max(answer_list))
#     print(answer_list.count(max(answer_list)))

# else:
#     print('SAD')
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit_list = list(map(int, input().split()))

# Edge case: if x is greater than n
if x > n:
    print("SAD")
    sys.exit()

# Calculate initial window sum
current_sum = sum(visit_list[:x])
max_sum = current_sum
max_count = 1

# Sliding window
for i in range(n - x):
    # Remove the leftmost element and add the new rightmost element
    current_sum = current_sum - visit_list[i] + visit_list[i + x] # 윈도우 하면서 빼고 더하면서 업데이트한다.
    
    if current_sum > max_sum:
        max_sum = current_sum
        max_count = 1
    elif current_sum == max_sum:
        max_count += 1

# Output results
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_count)