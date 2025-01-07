N,K=int(input()),int(input())
start,end=1,K

while start<=end:
    mid=(start+end)//2

    temp=0
    for i in range(1,N+1):
        temp+=min(mid//i,N) # 각 행에서 mid보다 작거나 같은 수의 개수를 계산


    if temp>=K: # 이분탐색 실행
        answer=mid
        end=mid-1
    else:
        start=mid+1

print(answer)

