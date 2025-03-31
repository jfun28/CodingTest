
def solution(players,m,k):
    server=[0]*len(players)
    cnt=0

    for i in range(len(players)):
        remain_p=players[i]-(server[i]*m) # 서버컴 써야하는데 못쓰는 사람
        if remain_p>=m: # 서버컴 써야하는데 못쓰는 사람이 증설해야하는 기준보다 높을때
            end=min(i+k,len(players)) # 끝을 체크하는 변수
            for j in range(i,end): 
                server[j]+=remain_p//m #서버컴 써야하는데 못쓰는 사람에서 증설해야하는 기준임계값 나눈데 서벌증설 필요갯수 그걸 기존 서버컴하고 더함
            cnt+=remain_p//m # 증설한 갯수를 더해가면서 결과값을 구한다



players=list(map(int,input().split()))
m=int(input())
k=int(input())


print(solution(players, m, k))

