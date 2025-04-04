def find_square(s):
    for i in range(n-s+1): # 행
        for j in range(m-s+1): #열
            if numbers[i][j]==numbers[i][j+s-1]==numbers[i+s-1][j]==numbers[i+s-1][j+s-1]:
                return True
    return False
 
n,m=map(int,input().split())

length=min(n,m)
numbers=[list(map(int,list(input()))) for _ in range(n)]

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(length,0,-1): # length 길이를 기점으로 줄여가면서 확인한다
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_square(k):
        print(k**2)
        break
    
