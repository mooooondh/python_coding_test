# 152p 미로탈출

from collections import deque

n, m= map(int, input().split())
maze= []
move_x= [-1, 0, 1, 0]
move_y= [0, 1, 0, -1]

for i in range(n):
    maze.append(list(map(int, input().split())))
    pass

def bfs(x, y):
    queue= deque()
    queue.append((x, y))

    while queue:
        x, y= queue.popleft()
        for i in range(4):
            dx= x+ move_x[i]
            dy= y+ move_y[i]

            if (dx< 0 or dy< 0 or dx>= n or dy>= m):
                continue
                pass
            if (maze[dx][dy]== 0):
                continue
                pass
            if (maze[dx][dy]== 1):
                maze[dx][dy]= maze[x][y]+ 1
                queue.append((dx, dy))
                pass
            pass    # end of for
        pass    # end of while
    return maze[n- 1][m- 1]
pass    # end of bfs

print(bfs(0, 0))