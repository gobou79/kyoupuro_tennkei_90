#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    if (H == 1) {
        cout << W << endl;
    }
    else if (W == 1) {
        cout << H << endl;
    }
    else {
        cout << ((H+1)/2) * ((W+1)/2) <<endl;
    }
}