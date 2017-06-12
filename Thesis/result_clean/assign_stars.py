import os
import csv
##----------------------------------------------------##
#                      給定顯著星號                     #
##----------------------------------------------------##
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\result\\panel_data')
with open('result_23.csv', 'rt') as file:
    sg = [x for x in csv.reader(file)]
## for 23 kinds
for x in range(1,7):
    for y in range(1,24):
        if 0.05< float(sg[x][y]) <0.06:
            sg[x][y] = sg[x][y] +'(.)'
        elif 0.01 < float(sg[x][y]) <=0.05:
            sg[x][y] = sg[x][y]+'(*)'
        elif 0.001 < float(sg[x][y]) <=0.01:
            sg[x][y] = sg[x][y]+'(**)'
        elif float(sg[x][y]) <= 0.001:
            sg[x][y] = sg[x][y]+'(***)'
with open('assign_star_23.csv', 'wt') as file:
    csv.writer(file, lineterminator='\n').writerows(sg)
## for 4 kinds
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\result\\panel_data')
with open('result_4.csv', 'rt') as file:
    sg = [x for x in csv.reader(file)]
for x in range(1,8):
    for y in range(1,5):
        if 0.05< float(sg[x][y]) <0.06:
            sg[x][y] = sg[x][y] +'(.)'
        if 0.01 < float(sg[x][y]) <=0.05:
            sg[x][y] = sg[x][y]+'(*)'
        elif 0.001 < float(sg[x][y]) <=0.01:
            sg[x][y] = sg[x][y]+'(**)'
        elif float(sg[x][y]) <= 0.001:
            sg[x][y] = sg[x][y]+'(***)'
with open('assign_star_4.csv', 'wt') as file:
    csv.writer(file, lineterminator='\n').writerows(sg)

## for total companies
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\result\\panel_data')
with open('result_overall.csv', 'rt') as file:
    sg = [x for x in csv.reader(file)]
for x in range(1,8):
    for y in range(1,2):
        if 0.05< float(sg[x][y]) <0.06:
            sg[x][y] = sg[x][y] +'(.)'
        if 0.01 < float(sg[x][y]) <=0.05:
            sg[x][y] = sg[x][y]+'(*)'
        elif 0.001 < float(sg[x][y]) <=0.01:
            sg[x][y] = sg[x][y]+'(**)'
        elif float(sg[x][y]) <= 0.001:
            sg[x][y] = sg[x][y]+'(***)'
with open('assign_star_overall.csv', 'wt') as file:
    csv.writer(file, lineterminator='\n').writerows(sg)

## for single_100_total companies
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\result\\single_100')
with open('result_100.csv', 'rt') as file:
    sg = [x for x in csv.reader(file)]
for x in range(1,8):
    for y in range(1,2):
        if 0.05< float(sg[x][y]) <0.06:
            sg[x][y] = sg[x][y] +'(.)'
        if 0.01 < float(sg[x][y]) <=0.05:
            sg[x][y] = sg[x][y]+'(*)'
        elif 0.001 < float(sg[x][y]) <=0.01:
            sg[x][y] = sg[x][y]+'(**)'
        elif float(sg[x][y]) <= 0.001:
            sg[x][y] = sg[x][y]+'(***)'
with open('assign_star_100.csv', 'wt') as file:
    csv.writer(file, lineterminator='\n').writerows(sg)

## for single_100_total companies
os.chdir('C:\\Users\\JIMMY\\Documents\\畢業論文\\data\\result\\single_95')
with open('result_95.csv', 'rt') as file:
    sg = [x for x in csv.reader(file)]
for x in range(1,7):
    for y in range(1,2):
        if 0.05< float(sg[x][y]) <0.06:
            sg[x][y] = sg[x][y] +'(.)'
        if 0.01 < float(sg[x][y]) <=0.05:
            sg[x][y] = sg[x][y]+'(*)'
        elif 0.001 < float(sg[x][y]) <=0.01:
            sg[x][y] = sg[x][y]+'(**)'
        elif float(sg[x][y]) <= 0.001:
            sg[x][y] = sg[x][y]+'(***)'
with open('assign_star_95.csv', 'wt') as file:
    csv.writer(file, lineterminator='\n').writerows(sg)
