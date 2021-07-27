#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, P, Q;
    cin >> N >> P >> Q;
    vector <int> A(N);
    for (int i = 0; i < N; i ++) cin >> A[i];

    int ans = 0;

    for (int i = 0; i<N; i++){
        for (int j = i+1; j<N; j++){
            for (int k = j+1; k < N; k++){
                for (int l = k+1; l < N; l++) {
                    for (int m=l+1; m < N; m++){
                        if (1LL * A[i] % P * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q) ans += 1;
                    }
                }
            }
        }
    }

    cout << ans << endl;

}