# -*- coding: utf-8 -*-


# usage:
# python sw_src sw_tgt useTop_n_src useTop_n_tgt from_src from_tgt to_src to_tgt

import sys
import re
import codecs

args = sys.argv
sw_ja = args[1]
sw_en = args[2]
useTop_n_ja = int(args[3])
useTop_n_en = int(args[4])
from_ja = args[5]
from_en = args[6]
to_ja = args[7]
to_en = args[8]

sw_ja_list = []
sw_en_list = []

for i, w in enumerate(codecs.open(sw_ja, 'r', 'utf-8')):
    # print(w.encode('utf-8'))
    if useTop_n_ja <= i:
        break
    w = w.strip().split('\t')[0]
    sw_ja_list.append(w)
for i, w in enumerate(codecs.open(sw_en, 'r', 'utf-8')):
    if useTop_n_en <= i:
        break
    w = w.strip().split('\t')[0]
    sw_en_list.append(w)

to_ja_file = codecs.open(to_ja, 'w', 'utf-8')
to_en_file = codecs.open(to_en, 'w', 'utf-8')

for ja_line, en_line in zip(codecs.open(from_ja,'r', 'utf-8'), codecs.open(from_en, 'r', 'utf-8')):
    ja_line = ja_line.strip()
    en_line = en_line.strip()
    ja_words = [w for w in ja_line.split(" ") if w not in sw_ja_list]
    en_words = [w for w in ja_line.split(" ") if w not in sw_ja_list]
    if ja_words == [] or en_words == []:
        continue
    ja_line = " ".join(ja_words)
    en_line = " ".join(en_words)
    to_ja_file.write(ja_line + '\n')
    to_en_file.write(en_line + '\n')
to_ja_file.close()
to_en_file.close()
