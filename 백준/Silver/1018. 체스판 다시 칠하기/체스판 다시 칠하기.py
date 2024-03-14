n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []
for i in range(n - 7):
    for j in range(m -7):
        change_black = 0
        change_white = 0
        
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0: 
                    if board[x][y] == "B":
                        change_black += 1
                    if board[x][y] == "W":
                        change_white += 1
                else: # 홀수일때 B
                    if board[x][y] == "W":
                        change_black += 1
                    if board[x][y] == "B":
                        change_white += 1
        result.append(min(change_white, change_black))
print(min(result))