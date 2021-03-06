void floydWarshall(int adj[n][n]) {
  int d[n][n]{};
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (i == j)
        d[i][j] = 0;
      else if (adj[i][j])
        d[i][j] = adj[i][j];
      else
        d[i][j] = INF;
    }
  }

  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }
}
