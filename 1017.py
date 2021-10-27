
# 最长上升子序列 LIS
# 状态表示:  集合: 所有以a[i] 结尾的严格单调递增的上升子序列
#           属性:Max
# 状态计算:  最后一步 f[i] = f[i] + f[k] - 1
N = 110
a = [0] * N
f = [0] * N
def solve():
  n = int(input())
  a = list(map(int,input().strip().split()))
  for i in range(n):
    f[i] = 1
    for k in range(i):
      if a[k] < a[i]:
        f[i] = max(f[i], f[k]+1)
  res = max(f)
  for i in range(n,-1,-1):
    f[i] = 1
    for k in range(n-1,i,-1):
      if a[k] < a[i]:
        f[i] = max(f[i], f[k]+1)
  res = max([res]+f)
  return res

if __name__ == "__main__":
  testcases = int(input())
  for caseNr in range(1, testcases + 1):
    # print("case %s" % (solve()))
    print("%s" % (solve()))

# 3
# 8
# 300 207 155 299 298 170 158 65
# 8
# 65 158 170 298 299 155 207 300
# 10
# 2 1 3 4 5 6 7 8 9 10
