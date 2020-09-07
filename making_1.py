# 217p 1로 만들기

# x= int(input())
# i= 1
# result= 0
#
# while(i!= x):
#     if(i* 5<= x):
#         i*= 5
#         result+= 1
#         pass
#     elif(i* 3<= x):
#         i+= 3
#         result += 1
#         pass
#     elif(i* 2<= x):
#         i*= 2
#         result += 1
#         pass
#     else:
#         result += 1
#         i+= 1
#         pass
#     pass
#
# print(int(result))

# 보텀업 다이나믹 프로그래밍
x= int(input())
d= [0]* 3001

for i in range(2, x+ 1):
    d[i]= d[i-1]+ 1

    if (i% 2== 0):
        d[i]= min(d[i], d[i//2]+ 1)
        pass
    elif (i %3 ==0):
        d[i]= min(d[i], d[i//3]+ 1)
        pass
    elif (i %5 ==0):
        d[i]= min(d[i], d[i//5]+ 1)
        pass
    pass

print(d[x])