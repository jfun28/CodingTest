import sys

input = sys.stdin.readline

n=int(input())
array=[]

count={}


for _ in range(n):
    x=int(input())
    array.append(x)
    
    if x not in count:
        count[x]=1
    else:
        count[x]+=1
            
    
array.sort()
answer=[]

# 평균값
mean=round(sum(array)/len(array))

# 중앙값
median=array[len(array)//2]

# 최빈값
freq=max(count.values())
numbers=[]

for key,items in count.items():
    if items==freq:
        numbers.append(key)

if len(numbers) == 1:
    two_bin=numbers[0]
else:
    numbers.sort()
    two_bin=numbers[1]

# 범위
arange=array[-1]-array[0]


print(mean)
print(median)
print(two_bin)
print(arange)

