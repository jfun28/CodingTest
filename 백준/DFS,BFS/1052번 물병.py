'''
같은 거 일때 물을 옮길 수 있다
'''
import sys
from collections import deque

n,k=map(int,input().split())

count=0

while bin(n).count("1")>k:
    n+=1
    count+=1


print(count)
