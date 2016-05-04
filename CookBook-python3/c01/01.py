#!/usr/bin/env python3

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for i in lines:
        if pattern in i:
            yield i, previous_lines
        previous_lines.append(i)

if __name__ == '__main__':
    with open(r'somefile.txt') as f:
      for line, prelines in search(f, 'python', 5):
        for pline in prelines:
            print(pline)
        print(line)
        print('-' * 20)
