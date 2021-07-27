#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B, C;
    cin >> N >> A >> B >> C;
    int ans = 9999;
    for (int i = 0; i < 10000; i++) {
        for (int j = 0; j< 10000; j++) {
            long long k = 1LL * N - A*i - B*j;
            if (k%C == 0 and k >= 0) {
                int candidate = i + j + (k / C);
                if (ans >= candidate) {
                    ans = candidate;
                }
            }
        }
    }
    cout << ans << endl;
}