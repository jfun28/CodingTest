# 카드 정렬하기
#힙정렬을 사용하면 deque랑 다르게 반복문을 이용해서 정렬할 필요없이 자동으로 정렬해준다. 

import sys
import heapq
input = sys.stdin.readline
n = int(input())
solution=[]
for i in range(n):
    heapq.heappush(solution,int(input()))

answer=0
while solution:
    if len(solution)<2:
        break
    v1 = heapq.heappop(solution)
    v2= heapq.heappop(solution)
    sum=(v1+v2)
    heapq.heappush(solution,sum)
    answer=answer+sum

print(answer)

