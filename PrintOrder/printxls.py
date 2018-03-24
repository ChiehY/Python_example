# -*- coding: utf-8 -*-
''''' 
 
main function：主要实现把txt中的每行数据写入到excel中 
'''  
  
#################  
#第一次执行的代码  
import xlwt #写入文件  
import xlrd #打开excel文件  
  
fopen=open("printorder.txt",'r')
  
lines=fopen.readlines() [7:61]
#新建一个excel文件  
file=xlwt.Workbook(encoding='utf-8',style_compression=0)  
#新建一个sheet  
sheet=file.add_sheet('sheet1')    
############################
i=0  
for line in lines:  
    sheet.write(i,0,line)   
    i=i+1
fopen2=open("printorder.txt",'r')  
lines2=fopen2.readlines() [74:140]
sheet2=file.add_sheet('sheet2')   
j=0  
for line in lines2:  
    sheet2.write(j,0,line)   
    j=j+1   
file.save('printorder.xls')