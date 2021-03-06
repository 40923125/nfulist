import requests
import bs4
# for os.environ and os.system
import os
# for geting html file path
import pathlib
  
# for pythn 3.9
proxy = 'http://[2001:288:6004:17::69]:3128'
  
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
  
'''
url:  'jclassroom_ajax.php',
data: { pselyr: pselyr, pselclssroom: pselclssroom },
'''
semester = '1092'
classroomno = 'BGA0901'
column = True
  
if semester == None:
    semester = '1092'
if classroomno == None:
    # BGA0611 電腦輔助設計室
    classroomno = 'BGA0901'
      
headers = {'X-Requested-With': 'XMLHttpRequest'}
  
url = 'https://qry.nfu.edu.tw/jclassroom_ajax.php'
post_var = {'pselyr': semester, 'pselclssroom': classroomno}
  
result = requests.post(url, data = post_var, headers = headers)
  
soup = bs4.BeautifulSoup(result.content, 'lxml')
  
# 先除掉所有 anchor
for a in soup.findAll('a'):
    # bs3 語法
    #a.replaceWithChildren()
    # bs4 語法, 將標註與內容拆開
    a.unwrap()
  
# 根據輸出設定, 取出 class='tbcls' 的 table 資料
table = soup.find('table', {'class': 'tbcls'})
  
# 重建 table, 設定邊線為 1 pixel
output = "<table border='1'>"
  
for i in table.contents:
    # 利用 replace 復原  
    output += str(i).replace("&nbsp", " ")
output += "</table>"
#print(output)
  
# 將 output 寫入 w1_classroom.html
fileName = "BGA0901.html"
with open(fileName, "w", encoding="utf-8") as file:
    file.write(output)
# 利用 os.system() 以 default browser 開啟 w1_class_local.html
filePath = pathlib.Path(__file__).parent.absolute()
#print(filePath)
# set firefox as default browser and start url to open html file
os.system("start file:///" + str(filePath) + "\\" + fileName)