# 149p 음료수 얼려 먹기

n, m= map(int, input().split())

result= 0

graph= []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x< 0 or y< 0 or x>= n or y>= m:
        return False

    if graph[x][y]== 0:
        graph[x][y]= 1
        # print("x= ", x, "y= ", y)

        dfs(x+ 1, y)
        dfs(x- 1, y)
        dfs(x, y+ 1)
        dfs(x, y- 1)
        return True
    return False
pass

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            pass
        pass
    pass

print(result)