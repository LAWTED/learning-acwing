N = int(input())
tri = []
for i in range(N):
  tmp = input().split()
  tmp = [int(i) for i in tmp]
  tri.append(tmp)
dp= [[0] * i for i in range(1,N+1)]
for i in range(N):
  dp[N-1][i] = tri[N-1][i]
for i in range(N-2,-1,-1):
  for k in range(i+1):
    dp[i][k] = max(dp[i+1][k],dp[i+1][k+1]) + tri[i][k]
print(dp[0][0])