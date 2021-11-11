import sys
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n     #par[x]:要素xの親頂点の番号（自身が根の場合は-1）
        self.rank = [0] * n     #rank[x]:要素xが属する根付き木の高さ
        self.siz = [1] * n    #siz[x]:要素xが属する根付き木に含まれる頂点数
    
    #根を求める
    def root(self, x):
        if self.par[x] == -1:   #xが根の場合はxを返す
            return x
        else:
            self.par[x] = self.root(self.par[x])    #経路圧縮
            return self.par[x]
    
    #xとyが同じグループに属するか（根が一致するか）
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    #xを含むグループとyを含むグループを併合する
    def unite(self, x, y):
        #x側とy側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False    #すでに同じグループのときは何もしない
        #union by size
        if self.rank[rx] > self.rank[ry]:   #ry側のrankが小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx   #ryをrxの子とする
        if self.rank[rx] == self.rank[ry]:  #rx側のrankを調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]    #rx側のsizを調整する
        return True
    
    #xを含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


H, W = map(int, input().split())
Q = int(input())

color = [False for i in range(H*W)]

uf = UnionFind(H*W)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j = q[1], q[2]
        num = (i-1)*W+(j-1)
        color[num] = True
        if num // W != 0:
            if color[num-W]:
                uf.unite(num, num-W)
        if num // W != (H-1):
            if color[num+W]:
                uf.unite(num, num+W)
        if num % W != 0:
            if color[num-1]:
                uf.unite(num, num-1)
        if num % W != W-1:
            if color[num+1]:
                uf.unite(num, num+1)
    else:
        a, b, c, d = q[1], q[2], q[3], q[4]
        num_1 = (a-1)*W+(b-1)
        num_2 = (c-1)*W+(d-1)
        if color[num_1]==False or color[num_2]==False:
            print("No")
        else:
            if uf.issame(num_1, num_2):
                print("Yes")
            else:
                print("No")