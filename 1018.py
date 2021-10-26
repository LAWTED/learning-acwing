N = int(input())
W = [[0] * (N+1)]
for i in range(N):
  tmp = [0] + list(map(int,input().split()))
  W.append(tmp)
# print(W)
f = [[0] * (N+1) for i in range(N+1)]
for i in range(1,N+1):
  for k in range(1,N+1):
    if i == 1 and k == 1:
      f[i][k] = W[i][k]
    else:
      f[i][k] = float('inf')
      if i > 1: f[i][k] = min(f[i][k],f[i-1][k]+W[i][k])
      if k > 1: f[i][k] = min(f[i][k],f[i][k-1]+W[i][k])
# print(f)
print(f[N][N])