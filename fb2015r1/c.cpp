#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    // cout << n;
    for (int i = 0; i < n; i++) {
        char str[100000];
        int a1, a2;
        cin >> str;
        sscanf(str, "%d-%d", &a1, &a2);
        cout << a1 << a2;
    }
}