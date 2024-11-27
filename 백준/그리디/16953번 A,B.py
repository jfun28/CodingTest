a,b=map(int,input().split())

count=1

while True:
    if b==a:
        print(count)
        break

    if b%2==0 and b//2 >= a:
        b=b//2
        count+=1
    elif b%10==1:
        b=b//10
        count+=1
    else:
        print(-1)
        break

#   if b%2==0 and  b//2 >= a: 나눠도 항상 a보다는 크다는 조건이 꼭 들어가 있어야한다.


