# 99p 1이 될 때까지

n, k= map(int, input().split())
result= 0

# while(True):
#     if(n% k!= 0):
#         n-= 1
#         result+= 1
#         if(n== 1):
#             break
#             pass
#         pass
#     else:
#         n/= k
#         result+= 1
#         if (n == 1):
#             break
#             pass
#         pass
#     pass
#
# print(result)

# 조금 더 빠르게

target= (n//k)* k
result+= n- target
while(True):
    if (n < k):
        break
        pass
    n//= k
    result+= 1
    pass

print(result)
