def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        # cache에 city가 있는 경우
            # 선택된 city cache에 제거 후에 다시 추가(갱신)
            # answer += 1

        for i in range(len(cache)):
            if cache[i] == city:
                cache.pop(i)
                cache.append(city)
                answer += 1
                break
        
        # cache가 city에 없는 없는 경우
            # cache가 가득 찬 경우
                # cache에서 가장 오래된 city 제거 --> pop(0)
                # 지금 city cache에 추가
                # answer += 5
            # cache가 가득 차지 않은 경우
                # 지금 city cache에 추가
                # answer += 5
        if city not in cache:
            if len(cache) == cacheSize:
                answer += 5
                cache.pop(0)
                cache.append(city)
            else:
                answer += 5
                cache.append(city)

    return answer



