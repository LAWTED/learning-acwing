N = 5010
a = [[10010] * 2 for i in range(N)]
f = [0] * N
def solve():
  n = int(input())
  for i in range(n):
    a[i][0], a[i][1] = map(int, input().split())
  a.sort(key=lambda x: x[0])
  # print(a)
  res = 0
  for i in range(n):
    f[i] = 1
    for k in range(i):
      if a[i][1] > a[k][1]:
        f[i] = max(f[i], f[k]+1)
    res = max(res, f[i])
  return res

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
  #   # print("case %s" % (solve()))
  #   print("%s" % (solve()))
  print("%s" % (solve()))