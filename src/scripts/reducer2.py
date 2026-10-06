#!/usr/bin/env python3
import sys
from collections import defaultdict

best = defaultdict(lambda: (None, 0))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        _, value = line.split('\t', 1)
        user, request, count = value.split('|')
        count = int(count)
    except ValueError:
        continue
    if count > best[user][1]:
        best[user] = (request, count)

results = sorted(
    [(count, user, request) for user, (request, count) in best.items()],
    reverse=True
)

for count, user, request in results[:4]:
    print(f"{user}\t{request}\t{count}")