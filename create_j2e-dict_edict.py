# coding: UTF-8

# usage:
# python create_j2e-dict_edict.py ~/src/corpus/EDICT/edict.tok.ja ~/src/corpus/EDICT/edict.tok.en ~/src/corpus/EDICT/j2e_dict.json

import sys
import json
import codecs

args = sys.argv
j2e_name = args[3]

j2e = {}
j2e_pruned = {}
prune_rate = 0.1
for ja_line, en_line in zip(codecs.open(args[1], 'r', 'utf-8'), codecs.open(args[2], 'r', 'utf-8')):
    ja_line = ja_line.strip()
    en_line = en_line.strip()
    ja_words = ja_line.split(" ")
    en_words = en_line.split(" ")
    for j_w in ja_words:
        for e_w in en_words:
            if j_w not in j2e:
                j2e[j_w] = {e_w : 1}
            else:
                if e_w not in j2e[j_w]:
                    j2e[j_w][e_w] = 1
                else:
                    j2e[j_w][e_w] += 1

print(type(j2e.items()[0][0]))    
for j, e in j2e.items()[:200]:
    print("{} : {}".format(j.encode('utf-8'), e))

for j_w, e_dict in j2e.items():
    e_sum = 0
    for e_cnt in e_dict.values():
        e_sum += e_cnt
    j2e_pruned[j_w] = [e_w for e_w, e_cnt in e_dict.items() if e_cnt > e_sum * prune_rate]
    if len(j2e_pruned[j_w]) == 0:
        del j2e_pruned[j_w]

print(len(j2e_pruned))    
for j, e in j2e_pruned.items()[:200]:
    print("{} : {}".format(j.encode('utf-8'), e))

f = codecs.open(j2e_name, "w", "utf-8")
json.dump(j2e_pruned, f, indent=2, sort_keys=True, ensure_ascii=False)
f.close()
