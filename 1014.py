# 预先处理从左往右的f[i]和从右往左的g[i] M[k] = f[k] + g[k] -1
# M[K]表示如果以K为最高峰的路径
N = 1010
f = [1] * N
g = [1] * N
def solve():
  n = int(input())
  w = list(map(int, input().split()))
  for i in range(n):
    for k in range(i):
      if w[k] < w[i]:
        f[i] = max(f[i], f[k]+1)
  for i in range(n-1,-1,-1):
    for k in range(n-1,i,-1):
      if w[k] < w[i]:
        g[i] = max(g[i], g[k]+1)
  res = 0
  for i in range(n):
    res  = max(res,f[i]+g[i]-1)
  return res

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
  #   print("%s" % (solve()))
  #   # print("case %s" % (solve()))
  print("%s" % (solve()))