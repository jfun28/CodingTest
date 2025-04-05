from itertools import combinations
h,w=map(int,input().split())
n=int(input())
max_n=0

stickers=[]
for _ in range(n):
    stickers.append(list(map(int,input().split())))

for comb in combinations(stickers,2):
    sticker1=comb[0]
    sticker2=comb[1]

    r1,c1=sticker1
    r2,c2=sticker2
    
    # 아무것도 돌리지지 않았을 때
    if (r1+r2<=h and max(c1,c2)<=w): 
        max_n=max(max_n,r1*c1+r2*c2)

    if (c1+c2<=h and max(r1,r2)<=w):
        max_n=max(max_n,r1*c1+r2*c2)

    # 두 번째 스티커만 돌릴 때
    if (r1+c2<=h and max(c1,r2)<=w): 
        max_n=max(max_n,r1*c1+r2*c2)

    if (max(r1,c2)<=h and c1+r2<=w):
        max_n=max(max_n,r1*c1+r2*c2)


    # 첫 번째 스티커만 돌릴 때
    if (c1+r2<=h and max(r1,c2)<=w):
        max_n=max(max_n,r1*c1+r2*c2)

    if (max(c1,r2)<=h and r1+c2<=w):
        max_n=max(max_n,r1*c1+r2*c2)


    # 둘다 회전
    if (c1+c2<=h and max(r1,r2)<=w): 
        max_n=max(max_n,r1*c1+r2*c2)
    
    if (max(c1,c2)<=h and r1+r2<=w):
        max_n=max(max_n,r1*c1+r2*c2)

 
print(max_n)





























# import sys
# input=sys.stdin.readline

# h,w=map(int,input().split())
# n=int(input())
# sticker=[]

# for _ in range(n):
#     r,c=map(int,input().split())
#     sticker.append([r,c])

# max_n=0
# for i in range(n):
#     r1=sticker[i][0] # 첫번쨰 스티커 높이
#     c1=sticker[i][1] # 첫번째 스티커 너비

#     for j in range(i+1,n):
#         r2=sticker[j][0] # 두번쨰 스티커 높이
#         c2=sticker[j][1] # 두번째 스티커 너비

#         # 모든 가능한 면접을 확인하면 된다.
#         if (r1+r2<=h and max(c1,c2)<=w) or (max(r1,r2)<=h and c1+c2<=w): # 1.두 스티커가 모두 회전하지 않은 경우
#             max_n=max(max_n, r1*c1+r2*c2)

#         # 2. 첫 번째 스티커는 그대로, 두 번째 스티커는 회전한 경우
#         elif (r1+c2<=h and max(c1,r2)<=w) or (max(r1,c2)<=h and c1+r2<=w):
#             max_n=max(max_n, r1*c1+r2*c2)

#         # 3. 첫 번째 스티커는 회전, 두 번째 스티커는 그대로인 경우
#         elif (c1+r2<=h and max(r1,c2)<=w) or (max(c1,r2)<=h and r1+c2<=w):
#             max_n=max(max_n, r1*c1+r2*c2)    

#         # 4. 첫 번째 스티커는 회전, 두 번쨰 스티커는 회전한 경우
#         elif (r1+r2<=w and max(c1,c2)<=h) or (max(r1,r2)<=w and c1+c2<=h):
#             max_n=max(max_n, r1*c1+r2*c2)   

# print(max_n)