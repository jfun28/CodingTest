import sys
input=sys.stdin.readline


n=int(input())
num_list=list(map(int,input().split()))


oper=list(map(int,input().split()))


min_num=1e9
max_num=-1e9

sum_num=0

def dfs(depth,sum_num,plus,minus,multiplly,divide):
    global max_num, min_num
    
    if depth==n:
        min_num=min(min_num,sum_num)
        max_num=max(max_num,sum_num)
        return

    if plus>0: # 플러스
        
        dfs(depth+1,sum_num+num_list[depth],plus-1,minus,multiplly,divide)

    if minus>0: # 마이너스
       
        dfs(depth+1,sum_num-num_list[depth],plus,minus-1,multiplly,divide)

    if multiplly>0: # 곱하기
        
        dfs(depth+1,sum_num*num_list[depth],plus,minus,multiplly-1,divide)

    if divide>0: # 나누기
        
        dfs(depth+1,int(sum_num/num_list[depth]),plus,minus,multiplly,divide-1)


dfs(1,num_list[0],oper[0],oper[1],oper[2],oper[3])

print(max_num)
print(min_num)