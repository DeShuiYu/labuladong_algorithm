# 5.12 Union-Find算法应用

本文对应的力扣题目：

[130.被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions)

[990.等式方程的可满足性](https://leetcode-cn.com/problems/surrounded-regions)

### 5.12.1 被围绕的区域

函数签名如下：

```java
void solve(char[][] board);
```

解决这个问题的传统方法就是 DFS 算法，先实现一个可复用的 `dfs` 函数，可以将 `O` 变成 `#`：

```java
/* 从 board[i][j] 开始 DFS，将字符 O 替换成字符 # */
void dfs(char[][] board, int i, int j) {
        int m = board.length, n = board[0].length;
        // 越界则直接返回
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return;
        }
        if (board[i][j] != 'O') {
            return;
        }
        // 进行替换
        board[i][j] = '#';
        // 向四周 DFS 搜索
        dfs(board, i + 1, j);
        dfs(board, i, j + 1);
        dfs(board, i - 1, j);
        dfs(board, i, j - 1);
}

void solve(char[][] board) {
    if (board.length == 0) return;
    int m = board.length, n = board[0].length;
    // 把第一行和最后一行关联的 O 变成 #
    for (int i = 0; i < m; i++) {
        dfs(board, i, 0);
        dfs(board, i, n - 1);
    }
    // 把第一列和最后一列关联的 O 变成 #
    for (int j = 0; j < n; j++) {
        dfs(board, 0, j);
        dfs(board, m - 1, j);
    }
    // 剩下的 O 都是应该被替换掉的
    for (int i = 1; i < m - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            }
        }
    }
    // 把所有字符 # 恢复成 O
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == '#') {
                board[i][j] = 'O';
            }
        }
    }
}
```

Union-Find 方法解决：

```java
void solve(char[][] board) {
    if (board.length == 0) return;

    int m = board.length;
    int n = board[0].length;
    // 给 dummy 留一个额外位置
    UF uf = new UnionFind(m * n + 1);
    int dummy = m * n;
    // 将首列和末列的 O 与 dummy 连通
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O')
            uf.union(i * n, dummy);
        if (board[i][n - 1] == 'O')
            uf.union(i * n + n - 1, dummy);
    }
    // 将首行和末行的 O 与 dummy 连通
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O')
            uf.union(j, dummy);
        if (board[m - 1][j] == 'O')
            uf.union(n * (m - 1) + j, dummy);
    }
    // 方向数组 d 是搜索上下左右四个方向的常用手法
    int[][] d = new int[][]{{1,0}, {0,1}, {0,-1}, {-1,0}};
    for (int i = 1; i < m - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            if (board[i][j] == 'O') {
                // 将此 O 与上下左右的 O 连通
                for (int k = 0; k < 4; k++) {
                    int x = i + d[k][0];
                    int y = j + d[k][1];
                    if (board[x][y] == 'O')
                        uf.union(x * n + y, i * n + j);
                }
            }
        }
    }
    // 现在，没有被 X 包围的 O 都和 dummy 连通了
    // 所有不和 dummy 连通的 O，都要被替换
    for (int i = 1; i < m - 1; i++) 
        for (int j = 1; j < n - 1; j++) 
            if (!uf.connected(dummy, i * n + j))
                board[i][j] = 'X';
}
```

### 5.12.2 判定合法等式

核心思想是，**将 `equations` 中的算式根据 `==` 和 `!=` 分成两部分，先处理 `==` 算式，使得他们通过相等关系相互「连通」；然后处理 `!=` 算式，检查不等关系是否破坏了相等关系的连通性**：

```java    
boolean equationsPossible(String[] equations) {
    // 26 个英文字母
    UF uf = new UnionFind(26);
    // 先让相等的字母形成连通分量
    for (String eq : equations) {
        if (eq.charAt(1) == '=') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            uf.union(x - 'a', y - 'a');
        }
    }
    // 检查不等关系是否打破相等关系的连通性
    for (String eq : equations) {
        if (eq.charAt(1) == '!') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            // 如果相等关系成立，就是逻辑冲突
            if (uf.connected(x - 'a', y - 'a'))
                return false;
        }
    }
    return true;
}
```