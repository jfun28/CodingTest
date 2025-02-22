eq=input().split('-')

num=[]

for i in eq:
    sum=0
    tmp=i.split('+')
    
    for j in tmp:
        sum=sum+int(j)
    num.append(sum)
    
result=num[0]    
for i in range(1,len(num)):
    result=result-num[i]
    
    
print(result)