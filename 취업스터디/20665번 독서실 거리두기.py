'''
1. 분으로 바꾸어서 계산
2. 전체 가용시간에서 할당된 시간을 뺴주는 방법으로 최종 답을 구한다


'''


n,t,p=map(int,input().split())

time=[]
for _ in range(t): # 시 분으로 되어 있는 것을 분 단위로 바꾼다.
    s,e=map(int,input().split())
    s=s//100*60+s%100
    e=e//100*60+e%100
    time.append((s,e)) # 시 분으로 바꿔준다.

time.sort() # 시간기준으로 정렬해준다.
ans=60*12 # 독서실 운영시간이 09:00~21:00라고 했으니 초기변수 최대 12시간으로 설정해둔다

def find_seat(arr): # 앉을 자리 선택
    if not arr:
        return 1    
    candidate=[] # 앉을 자리 후보
    if arr[0][0] !=1: # 1번 좌석이 비어 있는 경우
        candidate.append((arr[0][0]-1,1)) # (거리, 좌석번호)

    if arr[-1][0] !=n: # 마지막 n번이 비어있는 경우
        candidate.append((n-arr[-1][0],n)) # (가장끝-현재 거리, 좌석번호)
        
     # 사용 중인 좌석들 사이의 빈 공간 확인
    for i in range(1, len(arr)):
        # 현재 좌석과 이전 좌석 사이의 거리
        distance = arr[i][0] - arr[i-1][0]
        
        # 거리가 2 이상이면 중간에 앉을 수 있음 # 바로 옆이면은 중간에 앉을 수가 없다 
        if distance > 1:
            # 중간 좌석 계산 (중간에 여러 좌석이 있을 경우 거리의 절반 위치)
            mid_seat = arr[i-1][0] + distance // 2
            # 후보 목록에 (거리의 절반, 중간 좌석) 추가
            candidate.append((distance // 2, mid_seat))

    # 조건에 맞는 자리 1자리만 리턴    
    return sorted(candidate,key=lambda x:(-x[0],x[1]))[0][1] # 첫번쨰 기준: 거리가 큰 순서대로(-x[0]), 두 번째 기준: 좌석번호가 작은 순서대로(x[1])

used=[]

for s,e in time:
    new_used=[] # 현재(시간: s) 사용중인 좌석
    for u in used: # 퇴실한 좌석 걸러내기 
        if u[1]>s: # 해당 좌석의 종료 시간이 현재 시각보다 나중인가?",즉 아직 사용 중인 좌석이라면, 해당 좌석 정보를 new_used 리스트에 추가, 이미 퇴실했다면 new_used에 추가하지 않는다다
            new_used.append(u)
    res=find_seat(new_used)
    if res==p: # 민규가 좋아하는 자리에 누가 앉음
        ans-=(e-s) # 총 앉아 있을 수 있는 시간에서 다른 사람이 차지하고 있는 시간을 뺴서 총 앉아있을 수 있는 시간을 고른다
    new_used.append((res,e)) # find_seat 함수에서 결정된 좌석 번호, e는 현재 예약의 종료 시간
    used=sorted(new_used)  # 좌석번호 순서대로 정렬한다

print(ans)
 
















# import sys
# input=sys.stdin.readline
# times=[]

# N,T,P=map(int,input().split())

# for _ in range(T):
#     start,end=map(str,input().strip().split())
#     times.append([int(start),int(end)])
    
# times.sort(key=lambda x:(x[0],x[1]))
# last=[0]*(N+1)
# info=[[] for _ in range(N+1)]

# info[1].append(times[0])
# last[1]=times[0][1]

# for t in range(1,T):
#     start, end = times[t]
#     temp=[]
#     for i in range(1,N+1):
#         if start<last[i]:
#             temp.append(i)
            
#     maxDist=0
#     minIdx=1
    
#     for j in range(1,N+1):
#         v=101
#         for k in temp:
#             v=min(abs(j-k),v)
            
#         if v==0:
#             continue
#         if v>maxDist:
#             maxDist=v
#             minIdx=j
            
#     last[minIdx]=end
#     info[minIdx].append([start,end])
    
# result=720
# for i in range(len(info[P])):
#     s,e=info[P][i]
#     si,sj,ei,ej=s//100,s%100,e//100,e%100
#     if ei-sj<0:
#         val=(ei-si-1)*60+(60-(sj-ej))
        
#     else:
#         val=(ei-si)*60+(ej-sj)
        
#     result-=val
    
# print(result)