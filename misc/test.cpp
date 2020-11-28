#include <bits/stdc++.h>

using namespace std;

int main() {
    int v[8] = {-1, 2, 4, -3, 5, 2, -5, 2};
    auto n = 8;
    sort(v, v+n);
    for (auto i : v) {
        cout << i << ' ';
    }
    cout << endl;
}