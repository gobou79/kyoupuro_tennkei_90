#include <bits/stdc++.h>
using namespace std;

long long base8_to_long(string N) {
    long long res = 0, x = 1, M = N.size();
    for (int i = M-1; i >= 0; i--) {
        res += 1LL * int(N[i] - '0') * x;
        x *= 8LL;
    }
    return res;
}

string long_to_base9(long long N) {
    if (N == 0) {
        return "0";
    }
    string res;
    while (N>0) {
        res = char(N%9 + '0') + res;
        N /= 9;
    }
    return res;
}

int main() {
    string N; 
    int K;
    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        N = long_to_base9(base8_to_long(N));
        for (int j = 0; j < N.size(); j++) {
            if (N[j] == '8') {
                N[j] = '5';
            }
        }
    }
    cout << N << endl;
}
