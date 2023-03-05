import pymysql
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0) # 设置打印宽度(**重要**)

df2=pd.read_excel("成功案例.xlsx")
#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )
db=pymysql.connect(host="localhost",user="root", passwd="", db="testdb", charset="utf8")   
#建立操作游標
cursor = db.cursor()
#SQL語法（查詢資料庫版本）
sql = """SELECT * FROM scus
where purpose = "上課"
"""
#執行語法
cursor.execute(sql)

result = cursor.fetchall()
#執行結果轉化為dataframe
df = pd.DataFrame(list(result))



df.to_excel("只有上課.xlsx",index=False)
#關閉連線
db.close()

