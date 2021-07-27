N = int(input())
A, B, C = map(int, input().split())

ans = 9999

for i in range(10000):
    for j in range(10000):
        k = N - A*i - B*j
        if k % C == 0 and k >= 0:
            candidate = i + j + (k // C)
            if ans > candidate:
                ans = candidate

print(ans)