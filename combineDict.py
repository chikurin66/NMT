# -*- coding: utf-8 -*-


import sys
import json


def conbineDict(d_edict, d_mgiza):
    for s_w, t_w_l in d_edict.items():
        if s_w in d_mgiza:
            for t_w in t_w_l:
                if t_w in d_mgiza[s_w]:
                    d_mgiza[s_w][t_w] += 1
                else:
                    d_mgiza[s_w][t_w] = 1
        else:
            d_mgiza[s_w] = {}
            for t_w in t_w_l:
                d_mgiza[s_w][t_w] = 1
    return d_mgiza


if __name__ == "__main__":
    d_edict = json.load(open(sys.argv[1], 'r'))
    d_mgiza = json.load(open(sys.argv[2], 'r'))
    out_d_name = sys.argv[3]
    d = conbineDict(d_edict, d_mgiza)
    f = open(out_d_name, "w")
    json.dump(d, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))
    f.close()
