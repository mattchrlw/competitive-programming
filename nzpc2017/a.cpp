#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        int a;
        int b;
        int c;
        cin >> a >> b >> c;
        if (a + b + c == 180) {
            cout << a << " " << b << " " << c << " Seems OK" << endl;
        } else {
            cout << a << " " << b << " " << c << " Check" << endl;
        }
    }
    
}