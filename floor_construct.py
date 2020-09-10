# 223p 바닥공사

n= int(input())
result= 0
case_val= [0]* (n+ 1)
case_val[1]= 1
case_val[2]= 3

for i in range(3, n+ 1):
    case_val[i]= (case_val[i-1]+ case_val[i-2]* 2)% 796796
    pass

print(case_val[n])