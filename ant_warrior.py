# 220p 개미 전사

n= int(input())
food= list(map(int, input().split()))

arr= [0]* 100

arr[0]= food[0]
arr[1]= max(food[0], food[1])

for i in range(2, n):
    arr[i]= max(arr[i-1], arr[i -2]+ food[i])
    pass

print(arr[n- 1])