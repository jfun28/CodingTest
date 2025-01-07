# 집합 자료형 이용
n=int(input())

# 가게에 있는 전체 부품 번호를 입력받아서 집합 자료형에 기록
array=list(map(int,input().split()))

m=int(input())
x=list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인


for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')







# # 계수 정렬
# n=int(input())
# array=[0]*1000001

# # 가게에 있는 전체 부품 번호를 입력받아서 기록
# for i in input().split():
#     array[int(i)]=1


# # M(손님이 확인 요청한 부품 개수)을 입력받아서 기록
# m=int(input())
# # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분항 입력
# x=list(map(int,input().split()))

# for i in x:
#     if array[i]==1:
#         print('yes',end=' ')
#     else:
#         print('no',end=' ')









# def binary_search(array,target,start,end):
#     while start<=end:
#         mid=(start+end)//2
        
#         if array[mid]==target:
#             return mid
        
#         elif array[mid]>=target:
#             end=end-1
        
#         else:
#             start=start+1


#     return None




# n=int(input())

# array=list(map(int,input().split()))

# array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# m=int(input())
# array2=list(map(int,input().split()))

# for i in range(m):
#     if binary_search(array, array2[i],0, len(array))!=None:
#         print("yes",end=' ')
#     else:
#         print("no",end=' ')

