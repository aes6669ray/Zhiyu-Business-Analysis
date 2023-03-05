import pymysql
import pandas as pd
import numpy as np

df=pd.read_excel("成功案例.xlsx",)
df=df.where(df.notnull(),"NULL")


#資料庫連線設定
db=pymysql.connect(host="localhost",user="root", passwd="", db="test", charset="utf8")   
#建立操作游標
cursor = db.cursor()
#SQL語法（查詢資料庫版本）

#執行語法
# cursor.execute('''	CREATE TABLE IF NOT EXISTS companylist ( 
#             id int primary key,
# 			company char(100),
# 			address char(100),
#             item char(100),
#             CEO char(50)
# 			)
#        ''')
k=[]
for i in df.itertuples(index=False,name=None):
   k.append(i)

df2=pd.DataFrame(k,columns=df.columns)
#df2=df2.where(df2.notnull(),"NULL")
# print(k)

# sql='''INSERT INTO scuss (client, products, program, purpose, subtitle, NOTE, education) VALUES (%s,%s,%s,%s,%s,%s,%s)'''



# cursor.executemany(sql,k)


#cursor.executemany(sql, k)
db.commit()

#關閉連線
db.close()




