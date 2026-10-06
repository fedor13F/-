#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        key, count = line.split('\t', 1)
        user, request = key.split('|', 1)
        count = int(count)
    except ValueError:
        continue
    print(f"top\t{user}|{request}|{count}")