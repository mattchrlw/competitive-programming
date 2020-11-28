#include <bits/stdc++.h>

using namespace std;

int main() {
    string text;
    int freq[26] = { 0 };
    getline(cin, text);
    for (int i = 0; i < text.size(); i++){
        if (isalpha(text[i])) {
            freq[toupper(text[i]) - 'A']++;
        }
    }
    for (int i = 0; i < 26; i++) {
        cout << (char)('A' + i) << " | " << string(freq[i], '*') << endl;
    }
}