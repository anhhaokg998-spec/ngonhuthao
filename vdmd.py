def safe_squares_rooks(n, friend_rooks, enemy_rooks):
    board = [[0 for _ in range(n)] for _ in range(n)]

    for r, c in friend_rooks:
        board[r][c] = 1
    for r, c in enemy_rooks:
        board[r][c] = -1

    attacked = [[False for _ in range(n)] for _ in range(n)]

    for r, c in enemy_rooks:
        for i in range(r - 1, -1, -1):
            if board[i][c] != 0:
                break
            attacked[i][c] = True
        for i in range(r + 1, n):
            if board[i][c] != 0:
                break
            attacked[i][c] = True
        for j in range(c - 1, -1, -1):
            if board[r][j] != 0:
                break
            attacked[r][j] = True
        for j in range(c + 1, n):
            if board[r][j] != 0:
                break
            attacked[r][j] = True

    safe = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1 and not attacked[i][j]:
                safe += 1

    return safe
n = int(input("Nhập kích thước bàn cờ n: "))

f = int(input("Số xe phe ta: "))
friend_rooks = []
for _ in range(f):
    r, c = map(int, input("Nhập vị trí friend (r c): ").split())
    friend_rooks.append((r, c))

e = int(input("Số xe phe địch: "))
enemy_rooks = []
for _ in range(e):
    r, c = map(int, input("Nhập vị trí enemy (r c): ").split())
    enemy_rooks.append((r, c))

print("Số ô an toàn:", safe_squares_rooks(n, friend_rooks, enemy_rooks))