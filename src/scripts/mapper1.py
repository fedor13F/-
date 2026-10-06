#!/usr/bin/env python3
import sys
import re

def parse_line(line):
    m = re.match(r'^(\S+)\s+-\s+(\S+)\s+\[([^\]]+)\]\s+(\S+)\s+(\S+)', line)
    if not m:
        return None
    return m.group(2), f"{m.group(4)} {m.group(5)}"

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parsed = parse_line(line)
    if not parsed:
        continue
    user, request = parsed
    print(f"{user}|{request}\t1")
