N = 1010
f = [[0] * N for i in range(N)]
v = [0] * N
w = [0] * N
def solve():
  n, m = map(int, input().split())
  for i in range(1,n+1):
    v[i], w[i] = map(int,input().split())
  for i in range(1,n+1):
    for j in range(m+1):
      f[i][j] = f[i-1][j]
      if j >= v[i]:
        f[i][j] = max(f[i][j], f[i-1][j - v[i]] + w[i])
  # print(f)
  res = 0
  for i in range(m+1):
    res = max(res,f[n][i])
  return res


if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
    # print("case %s" % (solve()))
    # print("%s" % (solve()))
  print("%s" % (solve()))