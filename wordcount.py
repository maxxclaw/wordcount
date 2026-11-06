#!/usr/bin/env python3
"""Count lines, words and characters in files, like a small `wc`."""
import argparse
import sys


def count(text):
    return len(text.splitlines()), len(text.split()), len(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="files to count (default: stdin)")
    args = parser.parse_args(argv)

    if not args.files:
        print("%7d %7d %7d" % count(sys.stdin.read()))
        return 0
    for name in args.files:
        with open(name, encoding="utf-8") as f:
            print("%7d %7d %7d %s" % (*count(f.read()), name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
