A, B = map(int, input().split())

def gcd(a, b):
	while b != 0:
		a, b = b, a%b
	return a

if A > B:
    gcd = gcd(A, B)
else:
    gcd = gcd(B, A)

lcm = A * B // gcd

if lcm > 10 ** 18:
    print("Large")
else:
    print(lcm)