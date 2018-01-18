# coding: UTF-8

# usage:
# cat edict_file | python sentExt_iwslt.py out_file1 out_file2

import sys
import re

args = sys.argv
output1_filename = args[1]
output2_filename = args[2]

reg1 = re.compile("(\(.*?\))")
reg2 = re.compile("/")

e_m_dict = {}
for line in sys.stdin:
    sla_pos = line.find('/')
    # 見出し語
    entry = line[:sla_pos]
    entry = entry[:entry.find(' [')]
    # 意味
    mean = line[sla_pos+1:].strip().strip('/')
    mean = reg1.sub("", mean) # 丸括弧のものは消す
    mean = reg2.sub(" ", mean) # スラッシュを空白に置換 
    mean = mean.lower()
    mean_list = [w for w in mean.split(" ") if w != '']
    # entryの重複をなくすため辞書に
    if entry in e_m_dict:
        e_m_dict[entry].extend(mean_list)
    else:
        e_m_dict[entry] = mean_list

# 単語の重複をなくす
for k, v in e_m_dict.items():
    e_m_dict[k] = ' '.join(list(set(e_m_dict[k])))
    print(k + '|' + e_m_dict[k])
