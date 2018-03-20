from pprint import pprint
import string
import sys
import csv
import math
import pickle
import copy
from random import *

pro_kind_dic_old = pickle.load(open("./proj5.p","rb"))

states_type = {0:['T','F'], 1:['T','F'], 2:['T','F'], 3:['T','F'], 4:['T','B','M'], 5:['T','F'], 6:['T','F']}


with open('samples.Fill_the_missing.2017nov071410.txt','w', newline='') as csvfile:
    outputfile = csv.writer(csvfile, delimiter=' ')
    with open("./sample.pair.2017nov071410/samples.missing.2017nov071410.txt") as f:
        reader = csv.DictReader(f)
        for row in reader:
            field_flag = False
            each_row_list = []
            A = row['A']
            each_row_list.append(A)
            B = row['B']
            each_row_list.append(B)
            C = row['C']
            each_row_list.append(C)
            D = row['D']
            each_row_list.append(D)
            E = row['E']
            each_row_list.append(E)
            F = row['F']
            each_row_list.append(F)
            G = row['G']
            each_row_list.append(G)
#            print(each_row)

            for i in range(len(each_row_list)):
                if each_row_list[i] == 'NA':
                    field_flag = True
            if field_flag ==True:
                maybe_dic ={}
                for value in pro_kind_dic_old:
                    value_list = list(value)
                    falg = 0
#                    print(value)
                    for i in range(len(value_list)):
                        if each_row_list[i]!= 'NA':
                            if value_list[i] != each_row_list[i]:
                                falg +=1

                    if falg ==0:
#                        print(falg)
                        maybe_dic[value] = pro_kind_dic_old[value]
#                print(each_row_list)
#                pprint(maybe_dic)
                list_to_random = []
                for each_pro in  maybe_dic:
#                    print(each_pro)
                    the_times = int(maybe_dic[each_pro] *100)
                    for  i in range(the_times):
                        list_to_random.append(each_pro)
#                print(list_to_random)
                if len(list_to_random)==0:
                    for i in range(len(each_row_list)):
                        if each_row_list[i] == 'NA':
                            y = sample(states_type[i],1)
                            each_row_list[i] = y[0]
                    outputfile.writerow(each_row_list)
                else:
                    x = sample(list_to_random, 1)
                    x_split = list(x[0])
#                    print('x_split')
#                    print(x)
#                    print(x_split)
                    outputfile.writerow(x_split)
            else:
                outputfile.writerow(each_row_list)
#                print(each_row_list)





