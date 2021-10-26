走两次:
f[i1,j1,i2,j2] 表示所有的从(1,1)分别走到(i1,j1), (i2,j2)的路径的最大值
如何处理同一个格子不能被重复选择

if __name__ == "__main__":
  testcases = input()
  for caseNr in range(1, testcases + 1):
    print("%s" % (solve()))
def solve():

