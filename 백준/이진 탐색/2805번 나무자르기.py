n,m=map(int,input().split())

tree=list(map(int,input().split()))
tree.sort()
start=0
end=max(tree)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in tree:
        if x>mid:
            total+=(x-mid)

    # 나무의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
        end=end-1
    else: # 나무의 양이 넘치는 경우 조금 덜 자르기(오른쪽 부분 탐색)
        result=mid
        start=start+1



print(result)
