#!/usr/bin/python3
for k in range(122, 96, -1):
    print(chr(k) if k % 2 == 0 else chr(k-32), end='')
