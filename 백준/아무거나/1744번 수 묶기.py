n=int(input())

# plus : 양수데이터 리스트, minus 음수 데이터 리스트
'''
- 양수의 경우 가장 큰수를 기준으로 곱했을 때 큰 값이 나온다
- 음수의 경우 가장 작은수를 기준으로 곱했을 때 큰 값이 나온다
- 1은 무조건 더해주는 것이 수를 크게 만든다
- 0의 경우 음수들을 다 묶고남은 것이 있을 때 무조건 그값하고 곱해서 상쇄하는 것이 좋다
'''

plus=[]
minus=[]

result=0

for i in range(n):
    num=int(input())
    if num > 1:
        plus.append(num)
    elif num <=0:
        minus.append(num)
    else:
        result+=num


# 정렬
plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0,len(plus),2):
    if i+1>=len(plus):
        result+=plus[i]
    else:
        result+=(plus[i]*plus[i+1])

# 음수 묶기

for i in range(0,len(minus),2):
    if i+1>=len(minus):
        result+=minus[i]
    else:
        result+=(minus[i]*minus[i+1])


print(result)




    
