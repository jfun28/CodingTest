
# 국영수
import sys
input = sys.stdin.readline

n = int(input())
# 튜플이 있는 리스트를 sort 함수를 사용해 정렬하면  
st_list=[]
for i in range(n): 
    st_list.append(input().split())

st_list.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))


for student in st_list:
    print(student[0])
