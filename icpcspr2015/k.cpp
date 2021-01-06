#include <bits/stdc++.h>
#define N 1000000007L; // prime modulo value

using namespace std;

const string CODES = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

string to62(int value) {
    string str;
    while (value > 0) {
        str.insert(0, string(1, CODES[value % 62])); value /= 62;
    }
    return str;
}

int to10(string value) {
    reverse(value.begin(), value.end());
    int ret = 0;
    int count = 1;
    for (char& character : value) {
        ret += CODES.find(character) * count;
        count *= 62;
    }
    return ret;
}

int main() {
    while (!cin.eof()) {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            int a, b;
            string char1, char2, chars;
            cin >> chars;
            char1 = chars.substr(0, 3);
            char2 = chars.substr(3, 3);
            a = to10(char1); b = to10(char2);
            cout << a << " " << b << endl;
        }
    }
}