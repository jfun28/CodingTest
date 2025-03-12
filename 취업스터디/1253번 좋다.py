import sys 
sys.setrecursionlimit(10 ** 6)
n=int(input())
good_list=list(map(int,input().split()))
good_list.sort()

def binary_research(array,target,start,end,index,cnt):
    while start<=end:
        if array[start] + array[end] == target:
            if start==index: # 만약 0이 포함될때 자기자신이 좋은 수 만들기에 참여했다면 무시하여야한다.
                start=start+1
            elif end==index:
                end=end-1
            else:
                cnt=+1
                return cnt
        elif target<array[start] + array[end]:
            end=end-1
        else:
            start=start+1
    return 0

cnt=0
for index,i in enumerate(good_list):
    cnt+=binary_research(good_list,i,0,len(good_list)-1,index,cnt)
        

print(cnt)
    