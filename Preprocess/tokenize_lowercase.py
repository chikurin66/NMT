# -*- coding: utf-8 -*-

import sys
from collections import Counter

word_count = Counter()

args = sys.argv

for line in sys.stdin:
    line = line.rstrip('\n')
    line = line.replace('\r', '')
    line = line + ' '
    line = line.lower()   
    # put symbol between blanks
    line = line.replace('"', ' %dquote ')
    line = line.replace('“', ' %dquote ')
    line = line.replace('”', ' %dquote ')
    line = line.replace("„", ' %dquote ')
    line = line.replace("’", " %apostr ")
    line = line.replace("'", " %squote ")
    line = line.replace("\u0027", " %apostr ")
    line = line.replace("&#160;", " ")
    line = line.replace("amp#160;", " ")
    line = line.replace("&nbsp;", " ")
    line = line.replace("&amp;", " & ")
    line = line.replace("$", " $ ")
    line = line.replace("% ", " % ")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    line = line.replace("[", " [ ")
    line = line.replace("]", " ] ")
    line = line.replace("-", " - ")
    line = line.replace("&#45;", " - ")
    line = line.replace("amp#45;", " - ")
    line = line.replace(". ", " . ")
    line = line.replace(", ", " , ")
    line = line.replace(":", " : ")
    line = line.replace(";", " ; ")
    line = line.replace("/", " / ")
    line = line.replace(" #", " # ")
    line = line.replace("!", " ! ")
    line = line.replace("?", " ? ")
    # replace multiple blank space with a blank space
    line = line.replace("    ", " ")
    line = line.replace("   ", " ")
    line = line.replace("  ", " ")
    line = line.strip(' ')
    print(line)

