from flask import Flask, request 
from flask_cors import CORS
  
import requests
import bs4
#import ssl
  
'''
semester=1091

courseno=0762

cp

1a 1091/0762

1b 1091/0776

cad

2a 1091/0788

2b 1091/0801

https://nfulist.herokuapp.com/?semester=1082&courseno=0767
cd
2a 1082/0767
2b 1082/0780
  
2a 1072/0777
2b 1072/0790
2a 1062/0788
2a 1062/0802
  
wcm
1082/0744
  
1072/0754
1062/0765
  
wcmj
1082/2418
'''
  
app = Flask(__name__)
CORS(app)
  
@app.route('/studlist')
@app.route('/')
def studlist():
    semester = request.args.get('semester')
    courseno = request.args.get('courseno')
    column = request.args.get('column')

    if semester == None:
        semester = '1091'
    if courseno == None:
        courseno = '0762'
    
    headers = {'X-Requested-With': 'XMLHttpRequest'}

    url = 'https://qry.nfu.edu.tw/studlist_ajax.php'
    post_var = {'pselyr': semester, 'pseqno': courseno}
  
    result = requests.post(url, data = post_var, headers = headers)
    soup = bs4.BeautifulSoup(result.content, 'lxml')
    table = soup.find('table', {'class': 'tbcls'})
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    output = ""
    for i in data[2:]:
        #print(i[0])
        if column == "True":
            output +=i[0] + "</br>"
        else:
            output +=i[0] + "\n"
        
    return output
    #return  str(pselyr) + " + " +str(pseqno)
  
# 即使在近端仍希望以 https 模式下執行
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('localhost.crt', 'localhost.key')
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)