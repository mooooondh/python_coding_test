# 197p 부품 찾기

n= int(input())
parts= list(map(int, input().split()))
parts.sort()
m= int(input())
srch_parts= list(map(int, input().split()))

def binsearch(start, end, search, data):
    if(start> end):
        print("no", end= " ")
        return False

    mid = (start + end) // 2

    if(data[mid]== search):
        print("yes", end= " ")
        return True
    elif(data[mid]> search):
        binsearch(start, mid- 1, search, data)
        pass
    elif(data[mid]< search):
        binsearch(mid+ 1, end, search, data)
        pass
    pass

for i in srch_parts:
    binsearch(0, n, i, parts)
    pass
