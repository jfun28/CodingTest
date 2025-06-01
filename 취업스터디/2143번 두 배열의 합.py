from collections import Counter

T=int(input())
n=int(input())
A=list(map(int, input().split()))

m=int(input())
B=list(map(int,input().split()))

result=0 # 출력할 값으로 초기화
c=Counter() # 카운터 c 정의

for s in range(n):
    for e in range(s,n):
        c[sum(A[s:e+1])]+=1 # 배열 A의 모든 부배열의 합을 카운터에 개수로 센다

print("c",c)
        
for s in range(m):
    for e in range(s,m):
        t=T-sum(B[s:e+1]) # 타겟 값 T에서 B의 부배열합을 뺀 값이 
        result+=c[t] # A의 부배열에 존재하면 result에 더해준다. 없으면 저절로 0이 나온다.        
    
    
print(result)


