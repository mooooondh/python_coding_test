# 110p 상하좌우

n = int(input())
move = input().split()

move_type= ["L", "R", "U", "D"]
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

x, y, nx, ny= 1, 1, 0, 0

for i in move:
    for j in range(len(move_type)):
        if i== move_type[j]:
            nx= x+ move_x[j]
            ny= y+ move_y[j]
            pass
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
        pass
    x = nx
    y = ny
    pass

print(x, y)
