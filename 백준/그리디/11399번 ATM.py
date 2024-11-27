# 11399번 ATM
import heapq
n=int(input())

p_list=list(map(int,input().split()))
p_list.sort()

sum=0
for turn in range(n):
    for index in range(turn+1):
        value=p_list[index]
        sum=sum+value

print(sum)