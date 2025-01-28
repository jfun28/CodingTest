n=int(input())


b=list(map(int,input().split()))
count=0
while sum(b)!=0:
    check=0 # 이 단계를 설정함으로써 안에서 낱낱이 확인 하는 단계와 한번에 2로 나누는 단계로 분리할 수 있다.
    for i in range(n):
        if b[i]%2!=0 or b[i]==0: # 이도저도 확실히 짝수가 아닐때
            if b[i]==0: # 0일때면 그냥 그대로 진행한다. 
                continue
            else: # 정수인 홀수를 가질때
                b[i]-=1
                count+=1
            check=1 

    if check==0:
        b = list(map(lambda x: x/2, b))
        count+=1

print(count)