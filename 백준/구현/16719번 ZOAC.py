import sys

words = sys.stdin.readline().rstrip()

result = [''] * len(words)

def solve(input_words,start_idx):
    global result

    if input_words=='':
        return

    min_char=min(input_words)
    min_char_index=input_words.index(min_char)

    result[start_idx+min_char_index]=min_char
    print(''.join(result))
    
    solve(input_words[min_char_index+1:],start_idx+min_char_index+1)
        
    solve(input_words[:min_char_index],start_idx)


solve(words,0)

