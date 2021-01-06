#include <bits/stdc++.h>
#define N 1000000007L; // prime modulo value

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int k, n;
        cin >> n >> k;
        int l = n / 3;
        for (int j = 0; j < l; j++) {
            cout << "abc";
        }
        if (n - l * 3 == 2) {
            cout << "ab";
        } else if (n - l * 3 == 1) {
            cout << "a";
        }
        cout << endl;
    }
}