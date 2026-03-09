 #3129. Find All Possible Stable Binary Arrays I

class Solution:
  # Same as 3129. Find All Possible Stable Binary Arrays I
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    MOD = 1_000_000_007
    # dp[i][j][k] := the number of stable arrays, where the number of
    # occurrences of 0 is i and the number of occurrences of 1 is j and the last
    # number is k (0/1)
    dp = [[[0] * 2
           for _ in range(one + 1)]
          for _ in range(zero + 1)]

    for i in range(min(zero, limit) + 1):
      dp[i][0][0] = 1

    for j in range(min(one, limit) + 1):
      dp[0][j][1] = 1

    for i in range(1, zero + 1):
      for j in range(1, one + 1):
        dp[i][j][0] = (
            dp[i - 1][j][0] + dp[i - 1][j][1] -
            (dp[i - limit - 1][j][1] if i - limit >= 1 else 0) + MOD) % MOD
        dp[i][j][1] = (
            dp[i][j - 1][0] + dp[i][j - 1][1] -
            (dp[i][j - limit - 1][0] if j - limit >= 1 else 0) + MOD) % MOD

    return (dp[zero][one][0] + dp[zero][one][1]) % MOD
  
# Time Complexity: O(zero * one), where zero and one are the input parameters representing the number of occurrences of 0 and 1, respectively. We need to fill a 3D DP table of size (zero + 1) x (one + 1) x 2, which takes O(zero * one) time.
# Space Complexity: O(zero * one), as we are using a 3D DP table of size (zero + 1) x (one + 1) x 2 to store the number of stable arrays for different combinations of occurrences of 0 and 1.