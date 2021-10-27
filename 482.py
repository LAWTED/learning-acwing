# 1014登山的对偶
N = 110
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
  return n - res

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
  #   print("%s" % (solve()))
  #   # print("case %s" % (solve()))
  print("%s" % (solve()))