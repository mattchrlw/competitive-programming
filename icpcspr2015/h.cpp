#include <bits/stdc++.h>
#define INF LONG_MAX

using namespace std;

int main() {
    int w, h;
    cin >> w >> h;
    long long adj[w*h][w*h];
    // Initialise adjacency matrix
    for (int i = 0; i < w*h; i++) {
        for (int j = 0; j < w*h; j++) {
            adj[i][j] = INF;
        }
        // adj[i][i] = 0;
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            long long n; cin >> n;
            if (i*w+j-w >= 0) adj[i*w+j][i*w+j-w] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            long long n; cin >> n;
            // Modulus check (is it on the left edge?)
            if (i*w+j-1 >= 0 && (i*w+j)%w != 0) adj[i*w+j][i*w+j-1] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            long long n; cin >> n;
            if (i*w+j+w < h*w) adj[i*w+j][i*w+j+w] = n;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            long long n; cin >> n;
            // Modulus check (is it on the right edge?)
            if (i*w+j+1 < h*w && (i*w+j+1)%w != 0) adj[i*w+j][i*w+j+1] = n;
        }
    }
    int n = h*w;
    long long avg = 0;
    long long d[n][n];
    // Floyd-Warshall with negative edges
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // extra check for edges with weight 0
            if (i == j || (i != j && adj[i][j] == 0))
                d[i][j] = 0;
            else if (adj[i][j])
                d[i][j] = adj[i][j];
            else
                d[i][j] = INF;
        }
    }
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
    avg = avg/((hw2) - hw) + (avg % ((hw2) - hw) != 0);
    // avg = avg / ((h*w*h*w) - h*w);
    cout << avg;
}