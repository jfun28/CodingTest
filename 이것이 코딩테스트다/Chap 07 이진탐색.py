# import sys
# input_data=sys.stdin.readline().rstrip()

# print(input_data)


# #7-5.py

# def binary_search(array,target,start,end):
#     while start <=end:
#         mid=(start+end)//2
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid]==target:
#             return mid
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 
#         elif array[mid]>target:
#             end=mid-1
#         elif array[mid]<target:
#             start=mid+1
#     return None
    
# n=int(input())


# inventory=list(map(int,input().split()))
# inventory.sort()

# m=int(input())
# client=list(map(int,input().split()))


# for i in client:
#     # 해당 부품이 존재하는지 확인
#     result=binary_search(inventory,i,0,n-1)

#     if result!=None:
#         print('yes',end=' ')
    
#     else:
#         print('no',end=' ')


# # 3 실전문제 떡볶이 떡 만들기

# count, length=map(int,input().split(' '))

# array=list(map(int,input().split()))
# print("count",count)
# print("length",length)
# start=0
# end=max(array)
# print("end",end)
# def find_length(array,start,end):
#     while start<=end:
#         total=0
#         mid=(start+end)//2
#         for x in array:
#             if x-mid>0:
#                 total=total+(x-mid)
    
#         if total<length:
#             end=mid-1
#         else:
#             result=mid
#             print(result)
#             start=mid+1

#     print(result)
# find_length(array,start,end)
        


        