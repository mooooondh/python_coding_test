# 92p 큰 수의 법칙

n, m, k= map(int, input().split())
list= list(map(int, input().split()))
result= 0

list.sort(reverse= True)

# while(True):
#     for j in range(k):
#         if m<= 0:
#             break
#             pass
#         result+= list[0]
#         m -= 1
#         pass
#     if m <= 0:
#         break
#         pass
#     result+= list[1]
#     m -= 1

# 조금 더 빠르게

count= (m//(k+1))* k + (m% (k+1))
result+= count* list[0]
result+= (m- count)* list[1]


print(result)
