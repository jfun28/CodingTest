# 1. 우선은 양수랑 음수를 나누는 것이 핵심이다.
# 2. 그중 1초과, 0이하일 때를 나누고 1일때는 무조건 더하는게 이득이니깐 따로 뺴준다.
# 3. 0일 때는 어차피 있으면은 음수랑 같이 묶는 것이 편하니깐 음수쪽으로 분류해준다.

n=int(input())
plus=[]
minus=[]

result=0

for i in range(n):
    num=int(input())
    if num>1:
        plus.append(num)
    elif num<=0:
        minus.append(num)
    else:
        result+=num

# 정렬
plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0,len(plus),2):
    if i+1>=len(plus): # 마지막에는 곱할 쌍이 없어서 그대로 더함
        result+=plus[i]
    else:
        multi=plus[i]*plus[i+1]
        result+=multi

# 음수 묶기

for i in range(0,len(minus),2):
    if i + 1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i + 1]) # 0이 있다 한들 같이 곱하는게 최선의 방법이다.
print(result)

