#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

status_codes = {
    "200": 0, "301": 0, "400": 0,
    "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0
}
total_size = 0
line_count = 0


def print_stats():
    """Prints the accumulated stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        try:
            file_size = int(parts[-1])
            status = parts[-2]
            total_size += file_size
            if status in status_codes:
                status_codes[status] += 1
        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
