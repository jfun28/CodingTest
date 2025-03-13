import sys 
n=int(input())
good_list=list(map(int,input().split()))
good_list.sort()

def binary_research(array,target,start,end,index):
    cnt=0
    while start<end:
        if array[start] + array[end] == target:
            if start==index: # 만약 target변수가 자기자신일때는 포함 안시키고 건너 뛴다. 반례 0 0 0 1
                start=start+1
            elif end==index:
                end=end-1
            else:
                cnt+=1
                return cnt
        elif target<array[start] + array[end]:
            end=end-1
        else:
            start=start+1
    return 0

answer=0
for index, target in enumerate(good_list):
    cnt=binary_research(good_list,target,0,len(good_list)-1,index)
    answer+=cnt

print(answer)