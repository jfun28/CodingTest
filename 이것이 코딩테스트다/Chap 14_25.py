N=int(input())

step_ID=list(map(int,input().split()))

total=len(step_ID)
fail_ratio={}
for i in range(1,N+1):
    count=0
    for step in step_ID:
        if step==i:
            count+=1

    fail_ratio[i] = count/total
    total=total-count


answer = sorted(fail_ratio, key=lambda x : fail_ratio[x],reverse=True)
print(answer)
print(fail_ratio)