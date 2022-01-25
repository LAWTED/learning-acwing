# 最长上升子序列 LIS
# 状态表示:  集合: 所有以a[i] 结尾的严格单调递增的上升子序列
#           属性:Max
# 状态计算:  最后一步 f[i] = f[i] + f[k] + 1
N = 1010
a = [0] * N
f = [0] * N
def solve():
  n = int(input())
  a = list(map(int,input().split()))
  for i in range(n):
    f[i] = 1
    for k in range(i):
      if a[k] < a[i]:
        f[i] = max(f[i],f[k]+1)
  # print(f)
  res = max(f)
  return res

if __name__ == "__main__":
  # testcases = int(input())
  # for caseNr in range(1, testcases + 1):
    # print("%s" % (solve()))
  print("%s" % (solve()))