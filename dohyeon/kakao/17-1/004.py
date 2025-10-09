def solution(str1, str2):
    answer = 0
    str1_set = {}
    str2_set = {}
    
    for i in range(len(str1) - 1):
        if not str1[i].lower().isalpha() or not str1[i+1].lower().isalpha():
            continue
        if str1[i].lower()+str1[i+1].lower() in str1_set:
            str1_set[str1[i].lower() + str1[i+1].lower()] += 1
        else:
            str1_set[str1[i].lower() + str1[i+1].lower()] = 1
    
    for i in range(len(str2) - 1):
        if not str2[i].lower().isalpha() or not str2[i+1].lower().isalpha():
            continue
        if  str2[i].lower()+str2[i+1].lower() in str2_set:
            str2_set[str2[i].lower() + str2[i+1].lower()] += 1
        else:
            str2_set[str2[i].lower() + str2[i+1].lower()] = 1
    
    print(str1_set)
    print(str2_set)

    union = 0
    intersection = 0
    for key in str1_set:
        # key가 str2_set에 있으면 교집합과 합집합 계산, 없으면 합집합에만 추가
        if key in str2_set:
            union += max(str1_set[key], str2_set[key])
            intersection += min(str1_set[key], str2_set[key])
            str2_set.pop(key)
        else:
            union += str1_set[key]
    
    for key in str2_set:
        union += str2_set[key]

    if union == 0:
        answer = 1
    else:
        answer = intersection / union

    return int(answer * 65536)

# test
print(solution("FRANCE", "french"))  # 16384
print(solution("aa1+aa2", "AAAA12"))  # 43690