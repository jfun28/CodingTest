import sys
from collections import deque

q=deque()

input=sys.stdin.readline

T=int(input())

move=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def flip(change_arr,new_arr):
    for i in change_arr:
        new_arr[i]='0' if new_arr[i]=='1' else '1'

    return new_arr


def bfs(numbers):
    visited=[False]*512 # 512인 이유는 이코드에서 9비트 이진수를 다루고 있기 때문이다 
    visited[int(''.join(numbers),2)]=True

    q=deque([(int(''.join(numbers),2),0)])
    
    while q:
        n_num,count=q.popleft()
        if n_num==0 or n_num==511:
            return count
        
        for number in move:
            # 현재 상태에서 특정 행/열/대각선 뒤집기
            n_numbers = flip(number, list(bin(n_num)[2:].zfill(9))) #이진수 변환하면 앞의 '0b'를 제거 , 9자리가 되도록 앞쪽에 0을 채움, 3×3 = 9개 동전을 표현하기 위해
            n_num_bin=int(''.join(n_numbers),2)
            if not visited[n_num_bin]:
                visited[n_num_bin]=True
                q.append((int(''.join(n_numbers),2),count+1))

    return -1

            



for _ in range(T):
    graph=[]
    for _ in range(3):
        line = input().split()
        for coin in line:
            if coin == 'H':
                graph.append('0')  # 또는 '1'
            else:  # coin == 'T'
                graph.append('1')  # 또는 '0'
    

    print(bfs(graph))    
    