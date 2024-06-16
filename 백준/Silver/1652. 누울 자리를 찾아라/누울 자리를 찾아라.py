import sys
input  = sys.stdin.readline

def count_lie_down_places(grid):
    total_count = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if grid[i][j] == '.':
                count += 1
            else :
                if count >= 2:
                    total_count += 1
                count = 0
        if count >= 2:
            total_count += 1
            count = 0
    return total_count

N = int(input())
room = [input().rstrip() for _ in range(N)]
row = count_lie_down_places(room)
col = count_lie_down_places(list(zip(*room)))
print(row, col)