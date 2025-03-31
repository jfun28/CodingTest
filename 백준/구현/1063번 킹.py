king, stone, n=map(str,input().split())


move=[]
for _ in range(int(n)):
    move.append(input())


convert_alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
convert_alphabet_inverse = {v:k for k,v in convert_alphabet.items()} 

king_real=(int(king[1]),convert_alphabet[king[0]])
stone_real=(int(stone[1]),convert_alphabet[stone[0]])
print(king_real)

direction={"R":(0,1),"L":(0,-1),"B":(-1,0),"T":(1,0),"RT":(1,1),"LT":(1,-1),"RB":(-1,1),"LB":(-1,-1)}
k_y=king_real[0]
k_x=king_real[1]

s_y=stone_real[0]
s_x=stone_real[1]
for d in move :
    dy,dx=direction[d]
    king_ny=k_y+dy
    king_nx=k_x+dx

    stone_ny=s_y+dy
    stone_nx=s_x+dx

    if king_ny<1 or king_ny>8 or king_nx<1 or king_nx>8 :
        pass
    else:
        k_y=king_ny
        k_x=king_nx

    if stone_ny<1 or stone_ny>8 or stone_nx<1 or stone_nx>8 :
        pass
    else:
        s_y=stone_ny
        s_x=stone_nx


king_position=convert_alphabet_inverse.get(k_x)+str(k_y)

stone_position=convert_alphabet_inverse.get(s_x)+str(s_y)

print(king_position)
print(stone_position)



