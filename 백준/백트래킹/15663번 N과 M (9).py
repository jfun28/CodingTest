def dfs():
    if len(s)==m:
        current_combination=s.copy() 
        if current_combination not in memorable_list:
            memorable_list.append(current_combination) # 이렇게 해버리면 모두 동일한 S 객체를 가리키기 때문에 나중에 s.pop() 때문에 memorable_list에 아무것도 들어있지 않다.
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

visited=[False]*n

dfs()

# 정렬 후 출력
memorable_list.sort()

for value in memorable_list:
    print(*value)