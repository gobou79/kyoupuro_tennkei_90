def hantei(S):
    cnt = 0
    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1  
        else:
            cnt -= 1   
        if cnt < 0:
            return False 
    if cnt == 0:
        return True
    else:
        return False

N = int(input())

for i in range(1 << N):             #1<<Nは2^Nという意味
    candidate = ""
    for j in reversed(range(N)):        #reversedした理由は左から確認していくから（右から確認するときはreversedなし）
        if (i & (1 << j)) == 0:
            candidate += "("
        else:
            candidate += ")"
    h = hantei(candidate)
    if h == True:
        print(candidate)