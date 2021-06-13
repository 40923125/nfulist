import requests
import bs4
# for os.environ and os.system
import os
# for geting html file path
import pathlib
# 以下因應改為 Heroku based 程式所需導入模組,  修改步驟 1/6
from flask import Flask, request 
from flask_cors import CORS
 
 
# 修改步驟 2/6 , 加入 Flask 相關物件設定
app = Flask(__name__)
# 此一設定可以讓程式跨網域擷取資料
CORS(app)
 
# for pythn 3.9,  在近端測試時仍需要設定 proxy, 若使用 Python 3.8 執行則會自動使用系統的 Proxy 設定
'''
proxy = 'http://[2001:288:6004:17::69]:3128'
 
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
'''
'''
url:  'jclassroom_ajax.php',
data: { pselyr: pselyr, pselclssroom: pselclssroom },
'''
 
# 修改步驟 3/6, 試著將程式改為網際模式, 需要套用 Flask 的網際 decorator
@app.route('/')
def timeTableList():
    '''
    semester = '1092'
    classroomno = 'BGA0810'
    column = True
    '''
    semester = request.args.get('semester')
    classroomno = request.args.get('classroomno')

    if semester == None:
        semester = '1092'
    if classroomno == None:
        # BGA0810 電腦輔助設計室
        classroomno = 'BGA0810'
         
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
    # 修改步驟 5/6 , 因為已經將原先可列印出程式的步驟改為 function, 因此必須以 return 將擷取到的網頁資料傳回
    return output
@app.route('/git')
def timeTest():
     return "網際網路使用倉儲: <br /><br /><a href='https://github.com/40923125'>github</a></br><a href='https://dashboard.heroku.com/apps'>heroku</a>"
@app.route('/classroom6')
def timeTest1():
     return "BGA6樓: <br /><br /><a href='https://h40923125.herokuapp.com/?classroomno=BGA0611'>BGA0611</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0620'>BGA0620</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0640'>BGA0640</a>"
@app.route('/classroom7')
def timeTest2():
     return "BGA7樓: <br /><br /><a href='https://h40923125.herokuapp.com/?classroomno=BGA0710'>BGA0710</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0730'>BGA0730</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0760'>BGA0760</a>"
@app.route('/classroom8')
def timeTest3():
     return "BGA8樓: <br /><br /><a href='https://h40923125.herokuapp.com/?classroomno=BGA0820'>BGA0820</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0823'>BGA0823</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0830'>BGA0830</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0842'>BGA0842</a>"
@app.route('/classroom9')
def timeTest4():
     return "BGA9樓: <br /><br /><a href='https://h40923125.herokuapp.com/?classroomno=BGA0901'>BGA0901</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0911'>BGA0911</a></br><a href='https://h40923125.herokuapp.com/?classroomno=BGA0933'>BGA0933</a>"
@app.route('/classroom')
def timeTest5():
     return "109學年度第2學期BGA課表: <br /><br /><a href='https://h40923125.herokuapp.com/classroom6'>六樓</a></br><a href='https://h40923125.herokuapp.com/classroom7'>七樓</a></br><a href='https://h40923125.herokuapp.com/classroom8'>八樓</a></br><a  href='https://h40923125.herokuapp.com/classroom9'>九樓</a>"
     
# 修改步驟 4/6 , 因為改寫為網際程式後, 下列將內容存檔並自動呼叫 Firefox 的程式碼不再適用, 必須蓋掉
'''
# 將 output 寫入 w1_classroom.html
fileName = "w1_classroom.html"
with open(fileName, "w", encoding="utf-8") as file:
    file.write(output)
# 利用 os.system() 以 default browser 開啟 w1_class_local.html
filePath = pathlib.Path(__file__).parent.absolute()
#print(filePath)
# set firefox as default browser and start url to open html file
os.system("start file:///" + str(filePath) + "\\" + fileName)
'''
 
# 修改步驟 6/6, 配合網際程式啟動,  以及 Python 程式執行與納入其他程式執行的特定進行配置
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
