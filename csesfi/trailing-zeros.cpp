#include <bits/stdc++.h>
#define N 1000000007L; // prime modulo value

using namespace std;

int main() {
    long long n;
    cin >> n;
    long long count = 0;
    for (int i = 5; (n / i) > 0; i = i * 5) {
        count = count + n/i;
    }
    cout << count;
}