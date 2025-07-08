import sys
input=sys.stdin.readline



n=int(input())

array=list(map(int,input().split()))

op=list(map(int,input().split())) # +, -, *, /
maximum=-int(1e9)
minimum=int(1e9)

def dfs(depth,total,plus,minus,multiply,divide):
    global maximum,minimum
    
    if depth==n:
        minimum=min(total,minimum)
        maximum=max(total,maximum)

    if plus>0:
        dfs(depth+1,total+array[depth],plus-1,minus,multiply,divide)
    
    if minus>0:
        dfs(depth+1,total-array[depth],plus,minus-1,multiply,divide)

    if multiply>0:
        dfs(depth+1,total*array[depth],plus,minus,multiply-1,divide)

    if divide>0:
        dfs(depth+1,int(total/array[depth]),plus,minus,multiply,divide-1)

dfs(1,array[0],op[0],op[1],op[2],op[3])

print(maximum)
print(minimum)

