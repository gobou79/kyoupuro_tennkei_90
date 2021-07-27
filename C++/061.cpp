#include <bits/stdc++.h>
#include <deque>
using namespace std;

int main() {
    int Q;
    cin >> Q;
    int t, x;
    deque<int> d;
    for (int i=0; i<Q; i++) {
        cin >> t >> x;
        if (t == 1){
            d.push_front(x);
        }
        else if (t == 2){
            d.push_back(x);
        }
        else {
            cout << d[x-1] << endl;
        }
    }
}