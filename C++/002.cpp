#include <bits/stdc++.h>
using namespace std;

bool hantei(string S) {
    int dep = 0;
    for (int i = 0; i<S.size(); i++) {
        if (S[i] == '(') dep += 1;
        if (S[i] == ')') dep -= 1;
        if (dep < 0) return false;
    }
    if (dep == 0) return true;
    return false;
}

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < (1 << N); i++) {        //1<<Nは2^Nという意味（2**Nと同じ意味)
        string candidate = "";
        for (int j = N - 1; j >= 0; j--) {
            if ((i & (1 << j)) == 0) {              //左からbitが立っているか立っていないかをチェック
                candidate += "(";                   //0のとき '('
            }
            else {
                candidate += ")";                   //1のとき ')'
            }
        }
        bool I = hantei(candidate);
        if (I == true) cout << candidate << endl;
    }
}