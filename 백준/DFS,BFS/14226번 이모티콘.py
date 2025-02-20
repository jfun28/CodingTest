from collections import deque
s=int(input())

visited=[[0]*2001 for _ in range(2001)]

queue=deque()
queue.append([1,0,0]) # screen, clipboard, cnt


while queue:
    screen,clipboard,cnt=queue.popleft()
    if screen==s:
        print(cnt)
        break
    if screen>=1001 or clipboard>=1001 or visited[screen][clipboard]==1:
        continue

    # 여기서 부터는 방문하지 않은 경우
    visited[screen][clipboard]=1
    
    if screen>=1:
        queue.append([screen-1,clipboard,cnt+1])
        queue.append([screen,screen,cnt+1])

    if clipboard:
        queue.append([screen+clipboard,clipboard,cnt+1])

























# from collections import deque
# s=int(input())
# visited=[[0]*1001 for i in range(1001)]

# queue=deque()
# queue.append([1,0,0])

# while queue:
#     screen, clipboard, time=queue.popleft()
#     if screen==s:
#         print(time)
#         break
#     if screen>=1001 or screen <0 or clipboard >=1001 or clipboard < 0 or visited[screen][clipboard]:
#         continue
#     # 여기 부터는 한번도 방문하지 않은 경우의 수 

#     visited[screen][clipboard]=1
    
#     if screen>=1:
#         queue.append([screen-1,clipboard,time+1])
#         queue.append([screen,screen,time+1])

#     if clipboard: # 클립보드에 뭔가 있을 때
#         queue.append([screen+clipboard,clipboard,time+1])






















# from collections import deque
# import sys
# input=sys.stdin.readline

# s=int(input())

# queue=deque([[1,0,0]]) # 화면의 이모티콘 개수, 클립보드 이모티콘 개수, 연산 횟수

# visited=[[0]*1001 for _ in range(1001)]

# visited[1][0]=True

# while queue:
#     screen,clipboard,cnt=queue.popleft()
#     if screen == s # 만약 스크린의 개수와 s가 동일하다면
#         print(cnt)
#         break # 탈출

#     for i in range(3): # 연산을 3번 수행한다.
#         # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
#         if i==0:
#             new_screen,new_clipboard=screen,screen

#         # 화면에 클립보드에 있는 이모티콘 들을 추가
#         elif i==1:
#             new_screen, new_clipboard=screen+clipboard,clipboard
#         else: # 화면에 있는 이모티콘 개수 한개 빼기
#             new_screen, new_clipboard=screen-1,clipboard

#         # 만약 새로 계산된 이모티콘과 클립보드의 개수가 범위를 벗어나거나 이미 방문한 적이 있다면 continue
#         if new_screen>=1001 or new_screen <0 or new_clipboard >=1001 or new_clipboard < 0 or visited[new_screen][new_clipboard]:
#             continue

#         # 방문처리 후 연산 횟수를 +! 하여 큐에 추가
#         visited[new_screen][new_clipboard]=True
#         queue.append([new_screen,new_clipboard,cnt+1])



