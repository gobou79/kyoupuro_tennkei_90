#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> d(N);
    for (int i = 0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        if (a < b) {
            d[b-1] += 1;
        }
        else {
            d[a-1] += 1;
        }
    }
    int ans = 0;
    for (int i = 0; i<N; i++) {
        if (d[i] == 1){
            ans += 1;
        } 
    }

    cout << ans << endl;

}