# 状态表示 f[i] 集合 所有以a[i]结尾的上升子序列
#               属性 和的最大值
# 状态计算 f[i] = max(f[i] + )

N = 1010
f = [0] * N
def solve():
  n = int(input())
  a = [0] + list(map(int, input().split()))
  for i in range(1,n+1):
    f[i] = a[i]
    for k in range(1,i):
      if a[k] < a[i]:
        f[i] = max(f[i], f[k] + a[i])
  res = max(f)
  print(res)

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
  #   # print("case %s" % (solve()))
  #   print("%s" % (solve()))
  print("%s" % (solve()))