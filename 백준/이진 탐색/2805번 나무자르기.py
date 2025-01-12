import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 1. 나무 길이 정렬
trees.sort()

# 2. 누적 합(prefix sum) 준비
#    prefix_sum[i] = trees[0] + ... + trees[i-1]
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + trees[i-1]

# 잘린 나무 양을 계산하는 함수
def get_cut_wood(mid):
    # mid보다 큰 나무가 시작되는 인덱스 idx 찾기 (이진 탐색)
    idx = bisect.bisect_right(trees, mid)
    
    # idx부터 끝까지 있는 나무들을 잘랐을 때 총 길이
    # sum_of_tall_trees = prefix_sum[n] - prefix_sum[idx]
    # 잘린 길이 = sum_of_tall_trees - (mid * 잘린 나무의 개수)
    
    count_tall = n - idx  # mid보다 큰 나무 개수
    sum_tall_trees = prefix_sum[n] - prefix_sum[idx]
    cut_amount = sum_tall_trees - (mid * count_tall)
    
    return cut_amount

# 3. 이진 탐색
start, end = 0, max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    # mid로 잘랐을 때 얻는 나무 길이
    cut_amount = get_cut_wood(mid)
    
    if cut_amount < m:
        # 더 많이 잘라야 함 -> 절단기를 낮춤
        end = mid - 1
    else:
        # 충분히(혹은 넘치게) 잘렸으므로, 조금 덜 자를 수 있는 방향으로
        answer = mid  # 현재 mid로도 m 이상을 만족하므로 일단 저장
        start = mid + 1

print(answer)










# n,m=map(int,input().split())

# tree=list(map(int,input().split()))
# tree.sort()
# start=0
# end=max(tree)
# result=0
# while(start<=end):
#     total=0
#     mid=(start+end)//2
#     for x in tree:
#         if x>mid:
#             total+=(x-mid)

#     # 나무의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#     if total<m:
#         end=end-1
#     else: # 나무의 양이 넘치는 경우 조금 덜 자르기(오른쪽 부분 탐색)
#         result=mid
#         start=start+1



# print(result)
