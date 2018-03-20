from pprint import pprint
import string
import sys
import csv
import math
import pickle
import copy


import random
if sys.version_info[0] < 3:
    import Tkinter as tk #if python3, import tkinter
else:
    import tkinter as tk
    

all_kind_dic_old = pickle.load(open("proj5_2.p","rb"))

#ABCDEFG
each_state_dic = {0:['T','F'], 1:['T','F'], 2:['T','F'], 3:['T','F'],4:['T','B','M'], 5:['T','F'], 6:['T','F']}

order_list = [0,1,2,3,4,5,6]
#order_list = [4,0,5,3,6,1,2]
#order_list = [6,4,3,5,0,1,2]
#order_list = [0,2,3,5,1,6,4]

default_value = ['-','-','-','-','-','-','-']
order_string=['A','B','C','D','E','F','G']
adj = [['0' for x in range(7)] for y in range(7)]
total =[]
a = copy.deepcopy(default_value)

#change by order Ex.Order=EFGABCD -> P(E=T) = T------
def change_order(old_dic,order):
    new_dic = {}
    for value in old_dic:
        word_list = list(value)
        new_list_string  = ''
        for i in range(len(order)):
            new_list_string += word_list[order[i]]
        new_dic[new_list_string] = old_dic[value]
    return new_dic


#print(total)
def search_list (a,b):
    count = 0
    count_a = 0
    for j in range(len(a)):
        if a[j] =='-':
            count_a+=1
    for i in range(len(b)):
        if a[b[i]]== '-':
            count+=1
    if count == len(b) and count_a == len(b):
        return True
    else:
        return False
    

def input_one (a,b):
    a_list = list(a)
    for i in range(len(b)):
        a_list[b[i]] ='-'
    a_string = ''
    for j in range(len(a_list)):
        a_string+=a_list[j]
    return a_string


def search_friend(total, le):
    each_combine = []
    for i in range(1,int(math.pow(2,le))):
        a = '{0:07b}'.format(i)
        a_list = list(a)
        each_combine.append(a_list)
#    print(each_combine)
#    print(total)
    friend_dic = {}
    for i in range(len(total)):
        a_string_list = list(total[i])
#        print(a_string_list)
        friend_dic[total[i]] = {}
        for j in range(len(each_combine)):
            child_list =  copy.deepcopy(a_string_list)
            for k in range(len(each_combine[j])):
#            print('XOX')
#            print(child_list)
#            print(each_combine[j])
                if each_combine[j][k] =='0':
                    child_list[len(each_combine[j])-k-1] = '-'
            if child_list[(le-1)] !='-':
                temp_string = ''
                for l in range(len(child_list)):
                    temp_string += child_list[l]
#            print(temp_string)
#            print('OuO')
                if temp_string not in friend_dic[total[i]]:
                    if temp_string != '-------' and temp_string!=total[i]:
                        friend_dic[total[i]][temp_string] = 0
    return friend_dic


def change_b_s(ch_s,le):
    list_s = list(ch_s)
    list_s[(le-1)]='-'
    string_b_s = ''
    for i in range(len(list_s)):
        string_b_s+=list_s[i]
    return string_b_s


def change_to_b(friend):
    fr_li = list(friend)
    b_list = ['','','','','','','']
    for i in range(len(fr_li)):
        if fr_li[i]!='-':
            b_list[i]='1'
        else:
            b_list[i] ='0'
    b_st =''
    for j in range(len(b_list)):
        b_st+=b_list[j]
    
    return b_st


def wich_state(a,order):
    a_list = list(a)
    state_list = []
    for i in range(len(order)):
        if order[i]==0:
            state_list.append('A')
        if order[i] ==1:
            state_list.append('B')
        if order[i]==2:
            state_list.append('C')
        if order[i] ==3:
            state_list.append('D')
        if order[i] ==4:
            state_list.append('E')
        if order[i] == 5:
            state_list.append('F')
        if order[i] == 6:
            state_list.append('G')
#        state_list = ['A','B','C','D','E','F','G']
    final = []
    for i in range(len(a_list)):
        if a_list[i]=='1':
            final.append(state_list[i])
    final_string =''
    for j in range(len(final)):
        final_string += final[j]
    return final_string

    
def friend_love(friend_dic, le, all_kind_dic):
    friend_dic_copy ={}
    for i in friend_dic:
        if i in all_kind_dic:
            friend_dic_copy[i] = {}
#            print(i)
            for j in friend_dic[i]:
                if j in all_kind_dic:
                    must_string = change_b_s(j, le)
#                   print(must_string)
                    friend_dic[i][j] = float(all_kind_dic[j]/all_kind_dic[must_string])
                    temp_st = j+'/'+must_string
                    friend_dic_copy[i][temp_st] = friend_dic[i][j]
#                    print(j+'/'+must_string)
                else:
                    friend_dic[i][j]=0
        else:
            for j in friend_dic[i]:
                friend_dic[i][j]=0
#    pprint(friend_dic_copy)
#    pprint(friend_dic)
    return friend_dic


def have_connect(friend_ship, depend_ship,name,parend_1):
    count_de=0
    for value in depend_ship:
        attack = []
        for value2 in depend_ship[value]:
            attack.append(depend_ship[value][value2])
        if abs(attack[0]-attack[1])<0.002:###########################################################################
            count_de+=1
    print(count_de, len(depend_ship)*0.67)
    if count_de >= len(depend_ship)*0.67:
        print(name,' depends')
        return
    else:
#        print('in else')
        count ={}
        for value in friend_ship:
            for value2 in friend_ship[value]:
#                print (value2)
#                print(friend_ship[value][value2])
#                print(depend_ship[value][value])
                take_him_p = input_one(value,parend_1)
                if abs(friend_ship[value][value2]- depend_ship[value][take_him_p])<0.002:###################################
                    connect = change_to_b(value2)

#                print(value+"XoX"+value2+"OuO"+take_him_p)
#                    print(abs(friend_ship[value][value2]-depend_ship[value][take_him_p]))
                    if connect not in count:
                        count[connect] = 1
                    else:
                        count[connect]+=1
#                else:
#                    print(name, 'all connect')
        Flag = False
        if len(count) == 0:
#            print('len')
            print(name,'all_connect')
            for i in order_list:####################
                if (order_string[i] == name):
                    break
                if order_string[i] not in bayesian_network[name]['parents_list']:######################
                    bayesian_network[name]['parents_list'].append(order_string[i])######################
            #print ("bayesian_network[name]['parents_list']", bayesian_network[name]['parents_list'])############
            return
        for value2 in count:
#            print(count)
#            print(count[value2])
#            print(len(friend_ship)*0.66)
            if count[value2] >= len(friend_ship)*0.67:
                want_state = wich_state(value2,order_list)
#                print(want_state)
                print (name,' ',want_state, ' connect')
                want_state_list = list(want_state)
                for i in want_state_list:####################
                    if (i != name):
                        if i not in bayesian_network[name]['parents_list']:######################
                            bayesian_network[name]['parents_list'].append(i)######################
                #print ("bayesian_network[name]['parents_list']", bayesian_network[name]['parents_list'])############
                Flag = True
        if Flag == False:
            print(name, 'all connect')
            for i in order_list:####################
                if (order_string[i] == name):
                    break
                if order_string[i] not in bayesian_network[name]['parents_list']:######################
                    bayesian_network[name]['parents_list'].append(order_string[i])######################
            #print ("bayesian_network[name]['parents_list']", bayesian_network[name]['parents_list'])############


def put_it_in(list_a, list_b,list_c,which_one,len_p, all_kind_dic):
    parent_list =[]
    for value in all_kind_dic:
        a = list(value)
        b = list_a
        take = search_list(a,b)
        if take == True:
            parent_list.append(value)
    friend = search_friend(parent_list,len_p)
#    print(friend)
#    friend_score = friend_love(friend,len_p)
#    pprint(friend_score)
    temp = {}
    temp_2 ={}
    for value in friend:
#       for value2 in friend_score[value]:
        himself_no = list_b
        take_him = input_one(value,himself_no)
        take_him_p  = input_one(value,list_c)
#        print("him")
#        print(take_him )
        temp[value]={}
        temp[value][take_him] = (all_kind_dic[take_him]/1000000)
        temp[value][take_him_p] = (all_kind_dic[value]/all_kind_dic[take_him_p])
        temp_2[value]={}
        temp_s = value+'/'+take_him_p
        temp_2[value][take_him] = temp[value][take_him]
        temp_2[value][temp_s] = temp[value][take_him_p] 
#   for temp_value in temp:
#       for temp_value2 in temp[temp_value]:
#           friend_score[temp_value][temp_value2] = temp[temp_value][temp_value2]
#    pprint(friend_score)
        friend_score = {}
    for value in friend:
        friend_score[value]={}
        for value_2 in friend[value]:
            if value_2 not in temp[value]:
                friend_score[value][value_2] = 0
    friend_score_2 = friend_love(friend_score,len_p, all_kind_dic)
#    pprint(friend_score_2)
#    pprint(temp)
#    pprint(temp_2)
    have_connect(friend_score_2,temp,which_one,list_c)
    

#################################################################    
def drawCircle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def print_bayesian_network():
    win2=tk.Tk()
    win2.title("AI_midTerm4-5")
    win2.resizable(0,0)

    cvs = tk.Canvas(win2, width = 800, height = 800)
    cvs.grid(column=1,row=1)


    for item in bayesian_network:
        tk.Label(win2, bg=bayesian_network[item]['color'], text=item).place(x=(bayesian_network[item]['node_position_x']-10), 
                                                                            y=(bayesian_network[item]['node_position_y']-10))
        drawCircle(cvs, bayesian_network[item]['node_position_x'], bayesian_network[item]['node_position_y'], 20, fill = bayesian_network[item]['color'])
        
        #draw lines from parents to child
        for node_parents in bayesian_network[item]['parents_list']:
            cvs.create_line(bayesian_network[node_parents]['node_position_x'], bayesian_network[node_parents]['node_position_y'], 
                            bayesian_network[item]['node_position_x'], bayesian_network[item]['node_position_y'], 
                            fill = bayesian_network[node_parents]['color'], width=3, arrow = tk.LAST)

    win2.mainloop()
    
########################################################################


bayesian_network = {}
color_list=['blue','green','yellow','cyan','magenta','white','red']
scale = 100


for j in range(0, 7):
    bayesian_network[order_string[order_list[j]]] = {}
    bayesian_network[order_string[order_list[j]]]['color'] = color_list[j]
    bayesian_network[order_string[order_list[j]]]['parents_list'] = list()
    if((j%2) == 0):
        bayesian_network[order_string[order_list[j]]]['node_position_x'] = 50+ random.randint(0,99)
        bayesian_network[order_string[order_list[j]]]['node_position_y'] = 50+ scale*j
    else:
        bayesian_network[order_string[order_list[j]]]['node_position_x'] = 400+ random.randint(0,99)
        bayesian_network[order_string[order_list[j]]]['node_position_y'] = 50+ scale*j

    
    
print(order_list)    
    
all_kind_dic = change_order(all_kind_dic_old, order_list)

#add node1

#add node2
put_it_in([2,3,4,5,6],[0,2,3,4,5,6],[1,2,3,4,5,6],order_string[order_list[(2-1)]],2,all_kind_dic)

#add node3
put_it_in([3,4,5,6],[0,1,3,4,5,6],[2,3,4,5,6],order_string[order_list[(3-1)]],3,all_kind_dic)


#add node4
put_it_in([4,5,6],[0,1,2,4,5,6],[3,4,5,6],order_string[order_list[(4-1)]],4,all_kind_dic)

#add node5
put_it_in([5,6],[0,1,2,3,5,6],[4,5,6],order_string[order_list[(5-1)]],5, all_kind_dic)

#add node6
put_it_in([6],[0,1,2,3,4,6],[5,6],order_string[order_list[(6-1)]],6,all_kind_dic)

#add node7
put_it_in([],[0,1,2,3,4,5],[6],order_string[order_list[(7-1)]],7,all_kind_dic)


for item in bayesian_network:
    print ("bayesian_network[",item,"]['parents_list']", bayesian_network[item]['parents_list'])

print_bayesian_network()