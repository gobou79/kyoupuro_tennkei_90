import itertools

N = int(input())
A = []
kennaku = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    A.append(list(map(int, input().split())))

M = int(input())


for i in range(M):
    x, y = map(int, input().split())
    kennaku[x-1][y-1] = 1
    kennaku[y-1][x-1] = 1

arr = [i for i in range(N)]
arr_comb = list(itertools.permutations(arr, N))

ans = 10 ** 10  
k = -1

for i in range(len(arr_comb)):
    can = A[arr_comb[i][0]][0]
    for j in range(1, N):
        if kennaku[arr_comb[i][j-1]][arr_comb[i][j]] == 1:
            can = 10 ** 11
            break
        else:
            can += A[arr_comb[i][j]][j]
    if can < ans:
        ans = can      
        k = 1     

if k == -1:
    print(k)
else:
    print(ans)