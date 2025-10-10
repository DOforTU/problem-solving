def solution(dartResult):
    result = []
    for i in range(len(dartResult)):
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            result = calculate(dartResult[i], result)
        elif dartResult[i] == '*' or dartResult[i] == '#':
            result = calculate_option(dartResult[i], result)
        else:
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                result.append(10)
                i += 1
                continue
            result.append(int(dartResult[i]))
    return sum(result)

def calculate(op, result):
    if op == 'S':
        return result
    elif op == 'D':
        result[-1] = int(result[-1]) ** 2
        return result
    elif op == 'T':
        result[-1] = int(result[-1]) ** 3
        return result
    
def calculate_option(option, result):
    if option == '*':
        if len(result) == 1:
            result[0] *= 2
        else:
            result[-1] *= 2
            result[-2] *= 2
    elif option == '#':
        result[-1] *= -1
    
    return result


# test
print(solution("1T2D3D#"))  # 37