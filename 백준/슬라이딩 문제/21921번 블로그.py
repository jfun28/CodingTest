import sys
input=sys.stdin.readline

n,x=map(int,input().split())
visit_list=list(map(int,input().split()))
answer=0
answer_list=[0]

for i in range(n):
    temp=sum(visit_list[i:i+x])
    if temp==0:
        continue
    
    if answer<=temp:
        answer=temp
        answer_list.append(answer)

    # 여러 개가 최대값일 때는 어떻게 담을 것인가?

if max(answer_list)!=0:
    print(max(answer_list))
    print(answer_list.count(max(answer_list)))

else:
    print('SAD')
