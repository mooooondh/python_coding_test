# 180p 성적이 낮은 순서로 학생 출력하기

n= int(input())

grade= []
for i in range(n):
    data= input().split()
    grade.append((data[0], int(data[1])))
    pass

grade.sort(key= lambda std: std[1])

for i in grade:
    print(i[0], end= " ")
    pass