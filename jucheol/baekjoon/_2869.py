a,b,v = map(int, input().split())

days = (v - b) / (a - b)
if days != int(days):
    days = int(days) + 1
else:
    days = int(days)   

print(days)