import sys
from itertools import combinations, permutations 
input=sys.stdin.readline

n=int(input())

com=list(map(int,input().split()))

max_len=-int(1e9)

for i in range(len(com)+1):
    flag=True
    if i < 3:
        max_len=i
        continue

    for comb in combinations(com,i):
        flag=True
        for c in permutations(comb,3):
            if c[0]+c[1]<=c[2]:
                flag=False
                break

        if flag==True:
            max_len=max(max_len,i)
        

print(max_len)

