# 115p 왕실의 나이트

start= input()
row= ord(start[0])- 96
col= int(start[1])

row_m= [2, 2, -2, -2, 1, -1, 1, -1]
col_m= [1, -1, 1, -1, 2, 2, -2, -2]

result= 0

for i in range(len(row_m)):
    if(row+ row_m[i] >= 1 and row+ row_m[i]<= 8):
        if(col+ col_m[i] >= 1 and col+ col_m[i]<= 8):
            result+= 1
            pass
        pass
    pass

print(result)
