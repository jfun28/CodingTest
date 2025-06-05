n,m=map(int,input().split())

s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        print('s',s)
        dfs()
        print("s.pop",s.pop())

dfs()



# from itertools import product # 중복 순열로 풀기

# n, m = map(int, input().split())

# num_list = []

# for num in range(1, n+1):  # 1부터 n까지
#     num_list.append(num)

# for i in product(num_list, repeat=m):  # repeat=m 추가
#     print(*i)