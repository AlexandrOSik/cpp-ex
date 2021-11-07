import re
import sys

for line in sys.stdin.readlines():
 p = [int(i) for i in re.findall('[0-9]+', line)]
 l = [i + 1 for i in range(len(p) + 2)]
 print(p)
 for i in range(len(p)):
  v = next(i for i in l if i not in p)
  print(i + 1, ') ', v, ' <-> ', p[i])
  p[i] = None
  l[v - 1] = None
 u, v = [i for i in l if i is not None]
 print(len(p) + 1, ') ', u, ' <-> ', v)
