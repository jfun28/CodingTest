
def dfs(result,index):
    global min_result, max_result # 매 호출마다 독립적인 지역변수라면 → 이전 탐색 결과를 기억 못함
    # 마지막 index일때 종료
    if index==n-1:
        min_result=min(min_result,result)
        max_result=max(max_result,result)
        return
    
    for i in range(4):
        if four[i]!=0:
            four[i]-=1

            if i==0:
                dfs(result+arr[index+1],index+1)
            elif i==1:
                dfs(result-arr[index+1],index+1)
            elif i==2:
                dfs(result*arr[index+1],index+1)
            else:
                dfs(int(result/arr[index+1]),index+1)

            four[i]+=1


n=int(input())

arr=list(map(int,input().split()))

four=list(map(int,input().split()))


max_result = -1000000000
min_result = 1000000000

dfs(arr[0],0)

print(max_result)
print(min_result)



















# def dfs(result,index):
#     global min_result, max_result
#     # 마지막 index에 도착하였을 때
#     # 모든 사칙연산이 끝남
#     # 최대 최소 조사하여 갱신한다.

#     if index == n-1:
#         min_result = min(min_result, result)
#         max_result = max(max_result,result)
#         return

#     # 4개의 사칙연산에 대해서 탐색
#     for i in range(4):
#         # 사칙연산 남은 개수가 있으면
#         if four[i] != 0:
#             four[i] -= 1

#             if i == 0:
#                 dfs(result+arr[index+1],index+1)
#             elif i == 1:
#                 dfs(result-arr[index+1],index+1)
#             elif i == 2:
#                 dfs(result*arr[index+1],index+1)
#             else:
#                 dfs(int(result/arr[index+1]),index+1)

#             # return으로 돌아오면 이거 실행, 다른선택을 하기 위해 이전에 감소시킨 연산자 개수를 원래대로 복구해야함
#             four[i] += 1

# n = int(input())

# arr = list(map(int,input().split()))

# four = list(map(int,input().split()))

# min_result = 1000000000
# max_result = -1000000000

# dfs(arr[0],0)

# print(max_result)
# print(min_result)