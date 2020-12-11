# 2.19 动态规划和回溯算法，到底谁是谁爹

本文对应的力扣题目：

[494.目标和](https://leetcode.com/problems/target-sum)

函数的签名如下：

```java
int findTargetSumWays(int[] nums, int target);
```

### 2.19.1 回溯思路

```java
int result = 0;

/* 主函数 */
int findTargetSumWays(int[] nums, int target) {
    if (nums.length == 0) return 0;
    backtrack(nums, 0, target);
    return result;
}

/* 回溯算法模板 */
void backtrack(int[] nums, int i, int rest) {
    // base case
    if (i == nums.length) {
        if (rest == 0) {
            // 说明恰好凑出 target
            result++;
        }
        return;
    }
    // 给 nums[i] 选择 - 号
    rest += nums[i];
    // 穷举 nums[i + 1]
    backtrack(nums, i + 1, rest);
    // 撤销选择
    rest -= nums[i]; 
    
    // 给 nums[i] 选择 + 号
    rest -= nums[i];
    // 穷举 nums[i + 1]
    backtrack(nums, i + 1, rest);
    // 撤销选择
    rest += nums[i];
}
```

### 2.19.2 消除重叠子问题

状态 `(i, rest)` 是可以用备忘录技巧进行优化的：

```java
int findTargetSumWays(int[] nums, int target) {
    if (nums.length == 0) return 0;
    return dp(nums, nums.length - 1, target);
}

// 备忘录
HashMap<String, Integer> memo = new HashMap<>();
int dp(int[] nums, int i, int rest) {
    // base case
    if (i == nums.length) {
        if (rest == 0) return 1;
        return 0;
    }
    // 把它俩转成字符串才能作为哈希表的键
    String key = i + "," + rest;
    // 避免重复计算
    if (memo.containsKey(key)) {
        return memo.get(key);
    }
    // 还是穷举
    int result = dp(nums, i + 1, rest - nums[i]) + dp(nums, i + 1, rest + nums[i]);
    // 记入备忘录
    memo.put(key, result);
    return result;
}
```

### 2.19.3 动态规划

```java
int findTargetSumWays(int[] nums, int target) {
    int sum = 0;
    for (int n : nums) sum += n;
    // 这两种情况，不可能存在合法的子集划分
    if (sum < target || (sum + target) % 2 == 1) {
        return 0;
    }
    return subsets(nums, (sum + target) / 2);
}

/* 计算 nums 中有几个子集的和为 sum */
int subsets(int[] nums, int sum) {
    int n = nums.length;
    int[][] dp = new int[n + 1][sum + 1];
    // base case
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 1;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= sum; j++) {
            if (j >= nums[i-1]) {
                // 两种选择的结果之和
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
            } else {
                // 背包的空间不足，只能选择不装物品 i
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[n][sum];
}
```

然后，发现这个 `dp[i][j]` 只和前一行 `dp[i-1][..]` 有关，那么肯定可以优化成一维 `dp`：

```java
/* 计算 nums 中有几个子集的和为 sum */
int subsets(int[] nums, int sum) {
    int n = nums.length;
    int[] dp = new int[sum + 1];
    // base case
    dp[0] = 1;
    
    for (int i = 1; i <= n; i++) {
        // j 要从后往前遍历
        for (int j = sum; j >= 0; j--) {
            // 状态转移方程
            if (j >= nums[i-1]) {
                dp[j] = dp[j] + dp[j-nums[i-1]];
            } else {
                dp[j] = dp[j];
            }
        }
    }
    return dp[sum];
}
```

