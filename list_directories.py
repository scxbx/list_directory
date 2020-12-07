#!/usr/bin/python3

import os
from openpyxl import Workbook

# 打开文件
dirs = os.listdir()
real_dir_list = []
for my_dir in dirs:
    # if os.path.isdir(my_dir):
    if my_dir != 'list_directories.exe':
        real_dir_list.append(my_dir)

book = Workbook()
sheet = book.active

for i in range(len(real_dir_list)):
    sheet.cell(row=i+1, column=1).value = real_dir_list[i]
book.save('list_directories.xlsx')
