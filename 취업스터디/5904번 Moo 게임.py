import sys
n=int(input())















# # 새로운 차수=s(k-1)+o*k+m+s(k-1) 새로운차수 길이=전차수+1+k+2+전차수
# # 문자열의 길이와 규칙만으로 N번째 문자를 판별
# import sys

# n=int(input())

# s='moo'
# dp=[0] # 인덱스 정렬을 맞추기 위한 패딩용
# dp.append(3) # s(0)의 길이
# index=1 # s(k)의 길이가 n이상이 되는 최소한의 k를 찾는 과정
# while True: # while문은 S(k)의 길이가 n 이상이 되는 최소한의 k를 찾는 과정
#     dp.append(dp[index]+1+index+2+dp[index]) # 1(m)+0(k)+2dp[index]_len
#     if dp[-1]>=n:
#         break
#     index+=1

# nowIndex=len(dp)-1 # 위에서 찾은 dp의 마지막 인덱스를 nowIndex로 사용

# while True:   
#     if nowIndex==0: # 만약 현재 인덱스(맨앞) 도달했으면 출력
#         print(s[n-1]) # 최종적으로 s(0)에 도달했으면 'moo'인덱스 조회
#         break

#     if dp[nowIndex-1]<n<=nowIndex+2+dp[nowIndex-1]: # 가운데 "m"+"o"*(k+2) 부분
#         if n==dp[nowIndex-1]+1: #가운데 첫글자면 m 
#             print('m')
#             break 
#         else: # 그 외 글자면 o
#             print('o')
#             break

#     if dp[nowIndex-1]<n: # 오른쪽에 해당하는 경우 => 이렇게 하면 사실 왼쪽보다 클 경우 인데 이전 조건문에서 중앙 영역을 따졌으므로 오른쪽에 해당한다
#             n-=nowIndex+2+dp[nowIndex-1] # 오른쪽에 해당된다면 왼쪽과 중앙부분 잘라내고 n을 줄여서 탐색

#     nowIndex-=1 # 찾고자 하는 문자열의 차수
