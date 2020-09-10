# 226p 효율적인 화폐구성

n, m= map(int, input().split())
cash= []
for i in range(n):
    cash.append(int(input()))
    pass

result= [10001]* (m+ 1)
result[0]= 0

for i in range(1, m+ 1):
    for j in cash:
        if (i- j>= 0):
            result[i]= min(result[i], result[i- j]+ 1)
            pass
        pass
    pass

if (result[m]== 10001):
    print(-1)
    pass
else:
    print(result[m])