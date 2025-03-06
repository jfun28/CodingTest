import sys
input=sys.stdin.readline
n=int(input())
nums = list(map(int,input().split()))

nums.sort()

start=0
end=n-1

min_value=sys.maxsize

while start<end:
    take=nums[start]+nums[end]
    if abs(take)<min_value:
        min_value=abs(take)
        result=[nums[start],nums[end]]

    if take<0:
        start+=1
    elif take>0:
        end-=1
    else:
        break

print(result[0],result[1])











'''어떻게 0과 가까운 수인지 찾는 것이지?!?-> 절대값이 가장 작은 조합을 찾으면된다.'''
import sys
input=sys.stdin.readline

INF=int(10**6)

def closest_to_zero(nums):
    n = len(nums)
    min_sum = INF  # 초기값을 무한대로 설정
    closest_pair = None
    
    for i in range(n):
        for j in range(i+1, n):
            current_sum = nums[i] + nums[j]
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                closest_pair = (nums[i], nums[j])
    
    return closest_pair

n=int(input())
nums = list(map(int,input().split()))
pair= closest_to_zero(nums)
print(pair[0],pair[1])
