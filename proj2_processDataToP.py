from pprint import pprint
import string
import sys
import csv
import math
import pickle
import copy

each_combine = []
for i in range(1,int(math.pow(2,7))):
    a = '{0:07b}'.format(i)
    a_list = list(a)
    each_combine.append(a_list)
#print(each_combine)

#with open("./sample.pair.2017nov071410/samples.2017nov071410.txt" , 'r') as f:
with open("./sample.pair.2017nov071410/samples.Fill_the_missing.2017nov071410.txt",'r') as f:
    all_kind_dic ={}
    reader = csv.DictReader(f)

    for row in reader:
        each_row =[]
        #each_row_string = ''
        each_row.append(row['A'])
        each_row.append(row['B'])
        each_row.append(row['C'])
        each_row.append(row['D'])
        each_row.append(row['E'])
        each_row.append(row['F'])
        each_row.append(row['G'])

        for i in range(len(each_combine)):
            temp_each_row = copy.deepcopy(each_row)
            for j in range(len(each_combine[i])):
                if each_combine[i][j]=='0':
                    temp_each_row[j]='-'
 #           print(temp_each_row)
            each_row_string = ''
            for z in range(len(temp_each_row)):
                each_row_string += temp_each_row[z]
#            print(each_row_string)
            if each_row_string not in all_kind_dic:
                all_kind_dic[each_row_string]=1
            else:
                all_kind_dic[each_row_string]+=1
pickle.dump(all_kind_dic, open("proj5_2.p",'wb'))
pprint(all_kind_dic)

