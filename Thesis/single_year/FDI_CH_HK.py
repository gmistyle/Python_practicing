import os
import csv
from numpy import array
import numpy as np
##----------------------------------------------------##
#                  function definition                 #
##----------------------------------------------------##
def int_filter(data, index, lower, upper):#條件篩選函數
    tmp = []
    for x in data:
        if lower <= float(x[index]) < upper:
            tmp.append(x)
    print('data count:',len(tmp))
    return tmp

def write_in(file_name, data_name, title):#將篩選完的資料寫入新的檔案
    data_name.insert(0, title)
    with open(file_name,'wt') as file:
        a_out =csv.writer(file, lineterminator='\n')
        a_out.writerows(data_name)
##----------------------------------------------------##
#                    global_parameter                  #
##----------------------------------------------------##
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\single_100')
with open('single_100_ver1.csv', 'rt') as file:
    single = [x for x in csv.reader(file)]

title_single = single.pop(0)

ar_single = array(single)
cg_single = set(ar_single[:, 0])
##----------------------------------------------------##
#                        FDI_CH                        #
##----------------------------------------------------##
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\FDI\\single_year_FDI')
with open('FDI_CH.csv', 'rt') as file:
    CH = [x for x in csv.reader(file)]

title_CH = CH.pop(0)

need_CH = []#90~100年的FDI
for x in CH:
    if 9000 <= float(x[0]) < 10100:
        need_CH.append(x)

CH_94 = int_filter(need_CH, 0, 9400, 9500)
CH_95 = int_filter(need_CH, 0, 9500, 9600)
CH_99 = int_filter(need_CH, 0, 9900, 10000)
CH_100 = int_filter(need_CH, 0, 10000, 10100)

##----------------------------------------------------##
#                        FDI_HK                        #
##----------------------------------------------------##
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\FDI\\HonKong')
with open('FDI_HK.csv', 'rt') as file:
    HK = [x for x in csv.reader(file)]

title_HK = HK.pop(0)

need_HK = []#90~100年的FDI
for x in HK:
    if 9000 <= float(x[0]) < 10100:
        if x[1] == '香港':
            need_HK.append(x)

HK_94 = int_filter(need_HK, 0, 9400, 9500)
HK_95 = int_filter(need_HK, 0, 9500, 9600)
HK_99 = int_filter(need_HK, 0, 9900, 10000)
HK_100 = int_filter(need_HK, 0, 10000, 10100)

##----------------------------------------------------##
#                     mixed_CH_HK                      #
##----------------------------------------------------##
def category(data, index, dollar_index):#把各產業的當年度金額統整
    ar = array(data)
    cg = ar[:, index]
    d = {}
    for x in cg:#建立 {產業類別 : []} pair
        d[x] = []

    for x in data:# 歸納同類別的產業
        d[x[index]].append(float(x[dollar_index]))

    dd ={}
    for x in cg:
        dd[x] = sum(d[x])
    return dd

A = category(CH_94, 1, 2)
B = category(CH_95, 1, 2)
C = category(CH_99, 1, 2)
D = category(CH_100, 1, 2)

AA = category(HK_94, 2, 3)
BB = category(HK_95, 2, 3)
CC = category(HK_99, 2, 3)
DD = category(HK_100, 2, 3)

def mix(CH, HK):#把 CH 和 HK 的金額加起來
    cg_both = CH.keys() & HK.keys()
    cg_CH = CH.keys()
    d = {}
    for x in cg_CH:
        if x in cg_both:
            d[x] = CH[x]+HK[x]
        else:
            d[x] = CH[x]
    return d

AAA = mix(A, AA)
BBB = mix(B, BB)
CCC = mix(C, CC)
DDD = mix(D, DD)

##----------------------------------------------------##
#                     deflate data                     #
##----------------------------------------------------##
deflator_94 = 101.0364146
deflator_99 = 102.4
def deflate(data, deflator):
    cg = data.keys()
    tmp = {}
    for x in cg:
        tmp[x] = data[x]/deflator*100
    return tmp

AAA = deflate(AAA, deflator_94)
CCC = deflate(CCC, deflator_99)
##----------------------------------------------------##
# filter intersection between single_year_data and FDI #
##----------------------------------------------------##
final_cg = cg_single & CCC.keys() & DDD.keys() # use year 2010 and 2011 's intersection
title_out = title_single + ['lag_CH_HK', 'CH_HK', 'lag_CH', 'CH']
out = []
for x in single:
    if x[0] in final_cg:
        out.append(x+[CCC[x[0]], DDD[x[0]], C[x[0]], D[x[0]]])
out.insert(0, title_out)
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\single_100')
with open('single_100_ver2.csv', 'wt') as file:
    csv.writer(file, lineterminator = '\n').writerows(out)
