# coding: UTF-8

import sys

args = sys.argv

filename = args[1]
top_n = args[2]

# sys.stdout.write("top {} words from {}\n".format(top_n, filename))
num_unk = 0
for i, line in enumerate(open(filename, 'r')):
    line = line.strip()
    if i >= int(top_n):
        break
    print(line)
