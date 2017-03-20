#####打開檔案讀取原始資料
with open('panel_handmade.csv', 'rt') as file:
    a = csv.reader(file)
    data = [x for x in a]

title_panel = panel.pop(0)
#####條件篩選函數
def filter(data, index, condition):
    tmp = []
    for x in data:
        if x[index] == condition:
            tmp.append(x)
    print('data count:',len(tmp))
    return tmp
    
#filter(想參與篩選的data, 第幾欄, 篩選條件)

#####將篩選完的資料寫入新的檔案
def write_in(file_name, data_name):
    data_name.insert(0, title_data)##optional
    with open(file_name,'wt') as file:
        a_out =csv.writer(file, lineterminator='\n')
        a_out.writerows(data_name)

 #write_in(檔案名稱, 想要存的data):
