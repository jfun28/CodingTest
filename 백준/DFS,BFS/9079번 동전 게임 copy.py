import sys
from collections import deque

q=deque()

T=int(input())

move=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def flip(change_arr,new_arr):
    for i in change_arr:
        if new_arr[i]=='1':
            new_arr[i]='0'
        else:
            new_arr[i]='1'
        
    return new_arr


def bfs(numbers):

    visited=[False]*512 
    visited[int(''.join(numbers),2)]=True # 이진수인 수를 십진수로 변환하겠다.
    
    q=deque([(int(''.join(numbers),2),0)])

    while q:
        n_num, count=q.popleft()
        if n_num==0 or n_num==511:
            return count
        
        for move_numb in move:
            # 현재 상태에서 특정 행/열 대각선 뒤집기
            n_numbers=flip(move_numb,list(bin(n_num)[2:].zfill(9)))
            n_num_bin=int(''.join(n_numbers),2)
            if not visited[n_num_bin]:
                visited[n_num_bin]=True
                q.append((n_num_bin,count+1))

    return -1 


for _ in range(T):
    graph=[]
    for _ in range(3):
        line=input().split()
        for coin in line:
            if coin=='H':
                graph.append('0') 

            else:
                graph.append('1')

    print(bfs(graph))