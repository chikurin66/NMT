# coding: UTF-8

# usage:
# python sentExt_aspec.py in_file out_file1 out_file2

import sys

args = sys.argv
input_filename = args[1]
output1_filename = args[2]
output2_filename = args[3]

fo_ja = open(output1_filename, 'a')
fo_en = open(output2_filename, 'a')

# sys.stdout.write("top {} words from {}\n".format(top_n, filename))

train_flg = False
if "train" in input_filename:
    train_flg = True

for i, line in enumerate(open(input_filename, 'r')):
    line = line.strip() # stripをわすれずに
    try:
        if train_flg:
            _, _, _, sent_ja, sent_en = line.split(' ||| ')
        else:
            _, _, sent_ja, sent_en = line.split(' ||| ')
        fo_ja.write(sent_ja + '\n')
        fo_en.write(sent_en + '\n')
    except:
        print("error")
        print(line)

fo_ja.close()
fo_en.close()
