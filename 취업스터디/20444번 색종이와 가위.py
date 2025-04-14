n,k=map(int,input().split())
left=0
right=n//2
isPossible=False

while left <= right:
    rowCut=(left+right)//2
    colCut=n-rowCut

    # 가로, 세로 각각 rowcut, colCut번씩 잘랐다면 (rowCut+1)*(colCut+1) 조각이 생김
    pieces=(rowCut+1)*(colCut+1)

    if k==pieces:
        print('Yes')
        isPossible=True
        break

    if k>pieces: # 기존에 설정했던 것 보다 pieces가 더 적다 그렇다면
        left=rowCut+1
    else:
        right=rowCut-1

if not isPossible:
    print("No")