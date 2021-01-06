#include <bits/stdc++.h>
#define N 1000000007L; // prime modulo value

using namespace std;

long exp(long base, long exp) {
  long t = 1L;
  while (exp > 0) {
    if (exp % 2 != 0)
      t = (t * base) % N;
    base = (base * base) % N;
    exp /= 2;
  }
  return t % N;
}

int main() {
  long long n;
  cin >> n;
  cout << exp(2, n);
}