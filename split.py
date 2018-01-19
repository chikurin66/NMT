# coding: UTF-8

# usage:
# cat edict_file | python sentExt_iwslt.py

import sys
import re

args = sys.argv
ja = open(args[1], 'w')
en = open(args[2], 'w')

for line in sys.stdin:
     j_word, e_word = line.strip().split("||")
     ja.write(j_word + '\n')
     en.write(e_word + '\n')

ja.close()
en.close()
