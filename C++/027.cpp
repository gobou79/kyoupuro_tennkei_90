#include <bits/stdc++.h>
#include <map>
using namespace std;

int main() {
    map<string, int> d;
    int N;

    cin >> N;
    vector<string> S(N);
    for (int i=0; i<N;i++){
        cin >> S[i];
    }

    for (int i=0;i<N;i++) {
        if (d[S[i]] == 0){
            d[S[i]] = 1;
            cout << i+1 << endl;
        }
    }
}