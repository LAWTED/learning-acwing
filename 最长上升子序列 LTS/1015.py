#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
  R,C = map(int,input().split())
  w = [[0] * (C+1) for i in range(R+1)]
  for i in range(1,R+1):
    w[i] = [0] + list(map(int,input().split()))
  f = [[0] * (C+1) for i in range(R+1)]
  for i in range(1,R+1):
    for j in range(1,C+1):
      f[i][j] = max(f[i-1][j],f[i][j-1]) + w[i][j]
  return str(f[R][C])

if __name__ == "__main__":
  testcases = int(input())
  for caseNr in range(1, testcases + 1):
    # print("Case #%i: %s" % (caseNr, solve()))
    print("%s" % (solve()))