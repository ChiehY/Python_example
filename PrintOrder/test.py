from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import os



path = './PrintOrder.pdf'

# import pdf file
file = open(path, 'rb')
parser = PDFParser(file)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize()
resource = PDFResourceManager()
laparam = LAParams()
device = PDFPageAggregator(resource, laparams=laparam)
interpreter = PDFPageInterpreter(resource, device=device)

test = []
for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):
            test.append(out.get_text())


# pdf-green ['title', 'content', 'title', 'content'...]
grandContent = ''
grandList = []
for i in range(0, len(test)):
    tempList = []
    for chars in test[i]:
        if (chars == '\n' or chars == ':' or chars == '：'):
            grandContent.strip()
            tempList.append(grandContent)
            grandContent = ''
        else:
            grandContent += chars
    for contents in tempList:
        if (contents == ''):
            tempList.remove(contents)
    grandList.append(tempList)


# 数据处理
result = []

for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            resultTemp = grandfather[(i+2+len(str)):(i+2+len(str)+12)]
            result.append({content: resultTemp})
            break



for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            resultTemp = grandfather[(i+2+len(str)):(i+2+len(str)+10)]
            result.append({content: resultTemp})
            break



for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            TEMP = ''
            if (grandfather[i+len(str)+1] ==  '\n'):
                break
            else:
                for j in range(i+len(str), len(grandfather)):
                    if (grandfather[j] == '\n'):
                        break
                    if ((grandfather[j] == ' ') or (grandfather[j] == '：')):
                        continue
                    TEMP = TEMP + grandfather[j]
            result.append({content: TEMP})
            break



for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            TEMP = ''
            if (grandfather[i+len(str)+1] ==  '\n'):
                break
            else:
                for j in range(i+len(str), len(grandfather)):
                    if (grandfather[j] == '\n'):
                        break
                    if ((grandfather[j] == ' ') or (grandfather[j] == '：')):
                        continue
                    TEMP = TEMP + grandfather[j]
            result.append({content: TEMP})
            break



for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            TEMP = ''
            content = grandfather[i:i+len(str)-1]
            if (grandfather[i+len(str)+1] == '\n'):
                break
            else:
                for j in range(i+len(str), len(grandfather)):
                    if (grandfather[j+1] == '\n'):
                        break
                    if ((grandfather[j] == ' ') or (grandfather[j] == '：')):
                        continue
                    TEMP = TEMP + grandfather[j+1]
            result.append({content: TEMP})
            break



for grandfather in test:
    str = ''
    for i in range(0, len(grandfather)-len(str)):
        content = grandfather[i:i+len(str)]
        if (content == str):
            TEMP = ''
            content = grandfather[i:i+len(str)-1]
            if (grandfather[i+len(str)+1] ==  '\n'):
                break
            else:
                for j in range(i+len(str), len(grandfather)):
                    if (grandfather[j+1] == '\n'):
                        break
                    if ((grandfather[j] == ' ') or (grandfather[j] == '：')):
                        continue
                    TEMP = TEMP + grandfather[j+1]
            result.append({content: TEMP})
            break

# Check result
print(result, '\n\n')



keywords = ''
result_table = []
grandFather = grandList[2]
temp01 = grandFather[14:-3]
amount = int((len(temp01)-2)/3)

for x in range(0, amount-1):
    result_table.append([{temp01[0]: temp01[3*x+3]}, {temp01[1]: temp01[3*x+1+3]}, {temp01[2]:temp01[3*x+2+3]}])

result_table.append({temp01[-2]:temp01[-1]})
print(result_table, '\n\n')


keywords = ''
result_credit = []
for fff in range(0, len(grandList)-1):
    grandFather = grandList[fff]
    for i in range(0, len(grandFather)-1):
        father = grandFather[i]
        for j in range(0, len(father)-len(keywords)):
            if (father[j:j+len(keywords)] == keywords):
                real_name = grandList[fff+1]
                real_code = grandList[fff+2]
                real_time = grandList[fff+3]
                real_cost = grandList[fff+4]
                real_reim = []
                real_content = []
                real_reim.append(grandList[fff+5][0])
                real_content.append(grandList[fff+6][0])

                Content = ''
                for contents in grandList[fff+5][1:]:
                    for chars in contents:
                        if (chars == ' '):
                            real_reim.append(Content)
                            Content = ''
                        else:
                            Content += chars
                    real_content.append(Content)
                    Content = ''

for x in range(1, len(real_name)-1):
    result_credit.append([{'': real_name[x]}, {'': real_code[x]}, {'': real_time[x]}, {'': real_cost[x]}, {'': real_reim[x]}, {'': real_content[x]}])
print(result_credit, '\n\n')
