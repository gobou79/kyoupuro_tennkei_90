#include <bits/stdc++.h>
using namespace std;

long long gcd(long long x, long long y) {
    if(x > y){
        while (y > 0) {
            int r = x % y;
            x = y;
            y = r;
        }
        return x;
    }
    else {
        while (x > 0) {
            int r = y % x;
            y = x;
            x = r;
        }
        return y;
    }
}

int main() {
    long long A, B, C;
    cin >> A >> B >> C;
    long long l, g;
    l = gcd(A, B);
    g = gcd(l, C);
    long long ans = (A + B + C)/g - 3LL;
    cout << ans << endl;
}