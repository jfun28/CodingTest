max_gap = 0
answer = [-1]

def is_winner_with_gap(score, info):
    a = 0  # 어피치 점수
    b = 0  # 라이언 점수
    
    for i in range(len(info)): 
        if info[i] > 0 or score[i] > 0:
            if info[i] >= score[i]:
                a += (10-i)
            else:
                b += (10-i)
    return (b > a, abs(a-b))

def dfs(L, cnt, score, info, n):
    global max_gap, answer
    if L == 11 or cnt == 0: # 화살을 다 쏜 경우(모든 과녁을 다 검토하였거나 남은 화살의 개수 0개이거나) 
        is_winner, gap = is_winner_with_gap(score, info) 
        if is_winner:
            if cnt >= 0:  # 화살이 남은 경우
                score[10] = cnt  # 0점에 쏴도 이김
            
            if gap > max_gap:  # 갭이 더 큰 경우로 업데이트
                max_gap = gap
                answer = score.copy()
                
            elif gap == max_gap:  # 가장 낮은 점수를 많이 맞힌 경우로 업데이트
                for i in range(len(score)):
                    if answer[i] > 0:
                        max_i_1 = i
                    if score[i] > 0:
                        max_i_2 = i
                if max_i_2 > max_i_1:
                    answer = score.copy()
                
        return
    
    # k점을 어피치보다 많이 맞추거나 아예 안맞추거나 -> 점수를 더 높게 받거나 아예 포기하거나 후일을 노리거나
    if cnt > info[L]: # 현재 남은 화살이 어피치가 해당 점수에 쏜 화살 보다 많은지 확인
        score[L] = info[L]+1 # 어피치보다 1발 더 많이 쏘기로 결정
        dfs(L+1, cnt-(info[L]+1), score, info, n) # 다음 점수로 넘어감(L+1), 사용한 화살만큼 cnt에서 빼줌,현재까지의 점수 상태를 가지고 계속 탐색
        score[L] = 0 # 백트래킹 
        
    dfs(L+1, cnt, score, info, n) # 백트래킹으로 시도하는것 

def solution(n, info):
    global max_gap, answer
    
    answer = [-1]
    score = [0]*11
    max_gap = 0
    
    dfs(0, n, score, info, n)
    
    return answer