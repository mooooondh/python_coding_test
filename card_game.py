# 96p 숫자 카드 게임

n, m= map(int, input().split())
result= 0

for i in range(n):
    data= list(map(int, input().split()))
    if (min(data)> result):
        result= min(data)
        pass
    pass

print(result)