H, W = map(int, input().split())
A = []
B = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)
for i in range(H):
    b = list(map(int, input().split()))
    B.append(b)

cnt = 0

for i in range(H):
    for j in range(W):
        a = A[i][j]
        b = B[i][j]
        diff = b-a
        if j == W-1:
            if b-a != 0:
                print("No")
                exit()
        elif i == H-1:
            if b-a != 0:
                print("No")
                exit()
        else:
            cnt += abs(diff)
            A[i][j+1] += diff
            A[i+1][j] += diff
            A[i+1][j+1] += diff

print("Yes")
print(cnt)