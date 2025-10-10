def solution(s):
    answer = 1001
    
    # 사이즈를 1~len(s)까지 키우면서 각각의 압축 길이를 비교 후 최솟값을 출력
    for size in range(1, len(s)+1):
        # 압축된 문자열의 길이 구하는 로직이 필요
        cand_answer = press(size, s)
        answer = min(answer, cand_answer)
        
    return answer

def press(size, s):
    pressed_str = ''

    # s가 size랑 나누어 떨어지도록 ' '를 추가
    if len(s) % size != 0:
        s += ' ' * (size - (len(s) % size))
    
    cnt = 1
    current = s[0:size]
    for i in range(size, len(s)-size+1, size):
        current = s[i:i+size]
        before = s[i-size:i]
        
        if current == before:
            cnt += 1
        else:
            if cnt == 1:
                pressed_str += before
                cnt = 1
            else: 
                pressed_str += str(cnt)
                pressed_str += before
                cnt = 1
    
    # 마지막 남은 문자열 처리
    if cnt == 1:
        pressed_str += s[len(s)-size:len(s)]
    else:
        pressed_str += str(cnt)
        pressed_str += s[len(s)-size:len(s)]

    # 마지막으로 추가한 ' ' 제거
    pressed_str = pressed_str.replace(' ', '')

    return len(pressed_str)
    

# test
print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcabcabcdededededede"))  # 14