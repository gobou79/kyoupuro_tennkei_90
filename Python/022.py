import math

A, B, C = map(int, input().split())

l = math.gcd(A, B)
gcd = math.gcd(l, C)

ans = (A+B+C) // gcd -3

print(ans)
