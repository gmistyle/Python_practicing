import os

os.getcwd()# 取得當前的工作目錄

os.chdir("欲切換的路徑")# 切換目錄

new_path = os.path.join('A','B','C', ...)#組合路徑並自動加上兩條斜線 "\\"
