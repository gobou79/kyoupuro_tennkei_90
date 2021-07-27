N = int(input())
C = []
P = []
for i in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)
Q = int(input())
L = []
R = []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

S = [0]
T = [0]
s = 0
t = 0

for i in range(N):
    if C[i] == 1:
        s += P[i]
    else:
        t += P[i]
    S.append(s)  
    T.append(t)




for i in range(Q):
    ans_1 = S[R[i]] - S[L[i]-1]
    ans_2 = T[R[i]] - T[L[i]-1]
    print(ans_1, ans_2)
