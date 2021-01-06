#include <bits/stdc++.h>
#define N 1000000007L; // prime modulo value

using namespace std;

int main() {
  long long t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    long long y, x;
    cin >> y >> x;
    if (x > y) {
      if (x % 2 == 1) {
        cout << x * x - y + 1;
      } else {
        x--;
        cout << x * x + y;
      }
    } else {
      if (y % 2 == 0)
        cout << y * y - x + 1;
      else {
        y--;
        cout << y * y + x;
      }
    }
    cout << endl;
  }
}