def dfs():
    if len(s) == m:
        memorable_list.append(s.copy())
        return
    
    remember = 0
    for i in range(len(a_list)):
        if remember != a_list[i] and visited[i] == 0:
            visited[i]=True
            s.append(a_list[i])
            remember = a_list[i]
            dfs()
            visited[i] = False
            s.pop()

s=[]
memorable_list=[]
n,m=map(int,input().split())

a_list=list(map(int,input().split()))
a_list.sort()  # 미리 정렬해서 중복 제거와 순서 보장을 동시에

visited=[False]*n

dfs()



for value in memorable_list:
    print(*value)