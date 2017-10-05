# coding: UTF-8

# usage:
# python sentExt_iwslt_dev.py in_file1 in_file2 out_file1 out_file2

import sys
import xml.etree.ElementTree as ET

args = sys.argv
input1_filename = args[1]
input2_filename = args[2]
output1_filename = args[3]
output2_filename = args[4]

fo1 = open(output1_filename, 'w')
fo2 = open(output2_filename, 'w')

tree1 = ET.parse(input1_filename)
tree2 = ET.parse(input2_filename)
root1 = tree1.getroot()
root2 = tree2.getroot()
sent_list1 = root1.findall(".//seg")
sent_list2 = root2.findall(".//seg") 

# sys.stdout.write("top {} words from {}\n".format(top_n, filename))

for line1, line2 in zip(sent_list1, sent_list2):
    line1 = line1.text.strip()
    line2 = line2.text.strip()
    fo1.write(line1.encode('utf-8') + '\n')
    fo2.write(line2.encode('utf-8') + '\n')

fo1.close()
fo2.close()
