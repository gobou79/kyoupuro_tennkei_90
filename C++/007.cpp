#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    cin >> Q;
    vector<int> B(Q);
    for (int i = 0; i<Q; i++) cin >> B[i];

    sort(A.begin(),A.end());

    for (int i = 0; i<Q; i++) {
        if (B[i] > A[N-1]) {
            cout << B[i] - A[N-1] << endl;
        }
        else {
            auto position = lower_bound(A.begin(),A.end(), B[i]);
            if (position == A.begin()) {
                cout << *position - B[i] << endl;
            }
            else {
                cout << min(abs(*position - B[i]), abs(*(position-1)-B[i])) << endl;
            }
        }
    }
}