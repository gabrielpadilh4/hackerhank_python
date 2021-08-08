# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

regexp = r"([a-zA-Z0-9])\1+"

m = re.search(regexp, input())

if m:
    print(m.group(1))
else:
    print(-1)
