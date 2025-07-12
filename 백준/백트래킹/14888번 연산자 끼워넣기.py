import sys
input=sys.stdin.readline

n=int(input())
num_list=list(map(int,input().split()))

op=list(map(int,input().split()))
answer=0
min_ans=int(1e9)
max_ans=-int(1e9)

def search(depth, answer, plus, minus, multiply,divide):
    global min_ans,max_ans

    if depth==n:
        max_ans=max(max_ans, answer)
        min_ans=min(min_ans,answer)
        return

   
    if plus:
        search(depth+1, answer+num_list[depth], plus-1, minus, multiply,divide)


    elif minus:
        search(depth+1, answer-num_list[depth], plus, minus-1, multiply,divide)


    elif multiply:
        search(depth+1, answer*num_list[depth], plus, minus, multiply-1,divide)


    elif divide:
        search(depth+1, int(answer/num_list[depth]), plus, minus, multiply,divide-1)

search(1, num_list[0], op[0], op[1], op[2],op[3])

print(max_ans)
print(min_ans)