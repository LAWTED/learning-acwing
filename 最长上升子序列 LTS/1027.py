# 不能使用贪心的原因：
# 单次走的最大值之和，不是两次走的最大值

# 走两次:
# f[i1,j1,i2,j2] 表示所有的从(1,1)分别走到(i1,j1), (i2,j2)的路径的最大值
# 如何处理同一个格子不能被重复选择
# k = i1 + j1 = i2 + j2  曼哈顿距离
# f[k, i1, i2] 表示所有从(1,1)分别走到(i1,k-i1),(i2,k-i2)的路径的最大值
# 分析最后一步：
# 从上下来和从左过来的两种方式,两条路径，一共2 * 2= 4


def solve():
  n = int(input())
  N = 15
  w = [[0]*(N+1) for i in range(N+1)]
  while True:
    x,y,num = map(int,input().split())
    if x == 0 and y == 0 and num == 0:
      break
    w[x][y] = num
  K = 2 * n
  dp = [[[0 for k in range(N+1)]for i in range(N+1)]for j in range(2*N+1)]
  for k in range(2,K+1):
    for i1 in range(1,n+1):
      for i2 in range(1,n+1):
        j1, j2 = k - i1, k - i2
        if 1 <= j1 <= n and 1 <= j2 <= n:
          t = w[i1][j1]
          if (i1 != i2): t += w[i2][j2]
          dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2-1] + t)
          dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1-1][i2] + t)
          dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2-1] + t)
          dp[k][i1][i2] = max(dp[k][i1][i2], dp[k-1][i1][i2] + t)
  return dp[n+n][n][n]

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
  #   print("%s" % (solve()))
  print("%s" % (solve()))