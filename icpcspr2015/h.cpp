#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int main() {
    int w, h;
    cin >> w >> h;
    int d[w*h][w*h];
    // Initialise adjacency matrix
    for (int i = 0; i < w*h; i++) {
        for (int j = 0; j < w*h; j++) {
            d[i][j] = INF;
        }
        d[i][i] = 0;
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            int n; cin >> n;
            if (i*w+j-w >= 0) d[i*w+j][i*w+j-w] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            int n; cin >> n;
            // Modulus check (is it on the left edge?)
            if (i*w+j-1 >= 0 && (i*w+j)%w != 0) d[i*w+j][i*w+j-1] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            int n; cin >> n;
            if (i*w+j+w < h*w) d[i*w+j][i*w+j+w] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            int n; cin >> n;
            // Modulus check (is it on the right edge?)
            if (i*w+j+1 < h*w && (i*w+j+1)%w != 0) d[i*w+j][i*w+j+1] = n;
        }
    }
    int n = h*w;
    long long avg = 0;
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][k] < INF && d[k][j] < INF)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    for (int i = 0; i < w*h; i++) {
        for (int j = 0; j < w*h; j++) {
            avg += d[i][j];
        }
    }
    long long hw = h*w;
    long long hw2 = h*w*h*w;
    // Integer division without float cast
    avg = (avg + (hw2-hw) - 1)/(hw2-hw);
    // avg = avg / ((h*w*h*w) - h*w);
    cout << avg;
}