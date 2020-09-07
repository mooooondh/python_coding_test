# 182p 두 배열의 원소교체

n, k= map(int, input().split())

a= list(map(int, input().split()))
b= list(map(int, input().split()))

a.sort()
b.sort(reverse= True)

for i in range(k):
    if(a[i]< b[i]):
        a[i]= b[i]
        pass
    else:
        break
        pass
    pass

print(sum(a))