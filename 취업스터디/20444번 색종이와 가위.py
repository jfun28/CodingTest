n,k=map(int,input().split())
left=0
right=n//2
isPossible=False

while left<=right:
    rowCut=(left+right)//2
    colCut=n-rowCut

    piecies=(rowCut+1)*(colCut+1)

    if piecies==k:
        print('YES')
        isPossible=True
        break
            
    
    if piecies>k: # 좀 더 잘게 쪼개야한다
        right=right-1
    
    else: # 좀 더 러프하게 쪼개야한다
        left=left+1

if isPossible==False:
    print("NO")

    













































# n,k=map(int,input().split())
# left=0
# right=n//2 # 결과적으로 rowCut=x,colCut=n-x 또는 rowCut=n-x,colCut=x는 결과적으로 조각 수 가 똑같다
# isPossible=False

# while left <= right:
#     rowCut=(left+right)//2
#     colCut=n-rowCut

#     # 가로, 세로 각각 rowcut, colCut번씩 잘랐다면 (rowCut+1)*(colCut+1) 조각이 생김
#     pieces=(rowCut+1)*(colCut+1)

#     if k==pieces:
#         print('YES')
#         isPossible=True
#         break

#     if k>pieces: # 기존에 설정했던 것 보다 pieces가 더 적다 그렇다면=> 더 많이 잘라야 한다=> 가로로 좀 더 많이 자르면 조각 수가 늘어날 수 있다. 
#         left=rowCut+1
#     else: # 지금 자른 결과가 너무 많다 => 가로 자르는 횟수를 줄이려고 범위를 왼쪽으로 줄여줌
#         right=rowCut-1

# if not isPossible:
#     print("NO")