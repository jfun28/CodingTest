n,m=map(int,input().split())

n_list=[]
m_list=[]

for _ in range(n):
    n_list.append(input())

for _ in range(m):
    m_list.append(input())



def binary_search(array,target,start,end):
    while start<=end:
        