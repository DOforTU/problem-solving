def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        for i in range(len(cache)):
            if cache[i] == city:
                cache.pop(i)
                cache.append(city)
                answer += 1
                break
        if city not in cache:
            if len(cache) == cacheSize:
                answer += 5
                cache.pop(0)
                cache.append(city)
            else:
                answer += 5
                cache.append(city)

    return answer