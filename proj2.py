from pprint import pprint
import string
import sys
import csv
import math
import pickle

pro_kind_dic ={}
with open("./sample.pair.2017nov071410/samples.2017nov071410.txt",'r') as f:
    all_kind_dic = {}
#    pro_kind_dic = {}
    reader = csv.DictReader(f)
#    row_count = sum(1 for row in reader)
#    print(row_count)
    for row in reader:
#        print(DeprecationWarning)
        each_row = ''
        A = row['A']
        each_row += A
        B = row['B']
        each_row += B
        C = row['C']
        each_row += C
        D = row['D']
        each_row += D
        E = row['E']
        each_row += E
        F = row['F']
        each_row += F
        G = row['G']
        each_row += G

        if each_row not in all_kind_dic:
            all_kind_dic[each_row] = 1
        else:
            all_kind_dic[each_row] += 1
#    pprint(all_kind_dic)
    for value in all_kind_dic:
        pro_kind_dic[value] =  all_kind_dic[value]/1000000
pprint(pro_kind_dic)

pickle.dump(pro_kind_dic, open("proj5.p",'wb'))


