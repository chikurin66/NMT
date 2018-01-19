# coding: UTF-8

# usage:
# cat edict_file | python sentExt_iwslt.py

import sys
import re

args = sys.argv
sw_jp = args[1]
wakati_ja = args[2]
ext_en = args[3]
tok_ja = args[4]
tok_en = args[5]

sw_list = []
for w in open(sw_jp, 'r'):
    sw_list.append(w.strip())

ja_file = open(tok_ja, 'w')
en_file = open(tok_en, 'w')

for ja_line, en_line in zip(open(wakati_ja,'r'), open(ext_en, 'r')):
    ja_line = ja_line.strip()
    en_line = en_line.strip()
    ja_words = [w for w in ja_line.split(" ") if w not in sw_list]
    if ja_words == [] or en_line == "":
        continue
    ja_line = " ".join(ja_words)
    ja_file.write(ja_line + '\n')
    en_file.write(en_line + '\n')
ja_file.close()
en_file.close()
