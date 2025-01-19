from collections import deque
n=int(input())

n_list=list(map(int,input().split()))

m=int(input())

m_list=list(map(int,input().split()))

_dict={}
for i in range(len(n_list)):
    _dict[n_list[i]]=0

for j in range(m):
    if m_list[j] not in _dict:
        print(0,end=' ')
    else:
        print(1,end=' ')