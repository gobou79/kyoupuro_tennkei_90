H, W = map(int, input().split())

A = [list(map(int, input().split())) for l in range(H)]

B = [[0 for i in range(W)] for l in range(H)]

yoko = []
tate = []

for i in range(H):
    yoko.append(sum(A[i]))

for i in range(W):
    k = 0
    for j in range(H):
        k += A[j][i]
    tate.append(k)

for i in range(H):
    for j in range(W):
        B[i][j] = yoko[i] + tate[j] - A[i][j]
    print(*B[i])