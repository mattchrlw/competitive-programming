#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    long long n, m;
    m = 1;
    n = 1;
    cin >> s;
    for (int i = 1; i <= s.length(); i++) {
        if (s[i] == s[i-1]) {
            n += 1;
        } else {
            n = 1;
        }
        if (n > m) {
            m = n;
        }
    }
    cout << m;
}
