n=int(input())
data=sorted(list(map(int,input().split())))

if n>2:
    result=2
    for start in range(n-2):
        end=start+2
        while True:
            if data[start]+data[start+1]>data[end]:
                result=max(result,end-start+1)
                end+=1
                if end==n:
                    break
            else:
                break
    print(result)

else:
    print(n)




# import sys
# input=sys.stdin.readline

# n=int(input())

# num_array=list(map(int,input().split()))
# num_array.sort()

# if n<=2:
#     print(n)
#     exit()

# max_length=0

# # 모든 가능한 시작점에 대해
# for i in range(n):
#     # 각 시작점에서 가능한 끝점 찾기     
#     for j in range(i+2,n+1): # 최소 3개 원소 필요
#          # 현재 부분배열이 삼각수열인지 확인
#          # 정렬된 배열에서 가장 작은 두 수의 합이 가장 큰 수보다 크면 됨
#         if num_array[i]+num_array[i+1]>num_array[j-1]:
#             max_length=max(max_length,j-1)

#         else:
#         # 삼각관계를 만족하지 않으면 더 긴 구간도 만족하지 않음
#             break


# print(max_length)





