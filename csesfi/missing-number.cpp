#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n, m, i;
    cin >> n;
    m = n;
    for (i = 0; i < n - 1; i++) {
        long long a;
        cin >> a;
        m = m ^ i ^ a; 
    }
    cout << (m ^ i);
}