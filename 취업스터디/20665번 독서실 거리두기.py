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
    if arr[0][0] !=1: # 1번 좌석
        candidate.append((arr[0][0]-1,1))
    if arr[-1][0] !=n:
        candidate.append((n-arr[-1][0],n))
        
    for i in range(1,len(arr)):
        candidate.append((arr[i][0]))
        
    return sorted(candidate)



















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