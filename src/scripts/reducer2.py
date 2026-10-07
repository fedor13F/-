#!/usr/bin/env python3
import sys

results = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        _, value = line.split('\t', 1)
        user, request, count = value.split('|')
        results.append((int(count), user, request))
    except ValueError:
        continue

results.sort(reverse=True)

for count, user, request in results[:4]:
    print(f"{user}\t{request}\t{count}")