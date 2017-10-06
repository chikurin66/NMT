# coding: UTF-8

# usage:
# python sentExt_iwslt.py in_file1 in_file2 out_file1 out_file2

import sys

args = sys.argv
input1_filename = args[1]
input2_filename = args[2]
output1_filename = args[3]
output2_filename = args[4]

fo1 = open(output1_filename, 'w')
fo2 = open(output2_filename, 'w')

# sys.stdout.write("top {} words from {}\n".format(top_n, filename))

for in1, in2 in zip(open(input1_filename, 'r'), open(input2_filename, 'r')):
    in1 = in1.strip() # stripをわすれずに
    in2 = in2.strip() # stripをわすれずに
    if in1[0] != '<' and in2[0] != '<':
        fo1.write(in1 + '\n')
        fo2.write(in2 + '\n')
fo1.close()
fo2.close()
