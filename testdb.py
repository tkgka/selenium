import pymysql
pw = "root"
conn = pymysql.connect(host='10.0.10.78', user='root', password=pw, charset='utf8')
curs = conn.cursor()
print("no error")