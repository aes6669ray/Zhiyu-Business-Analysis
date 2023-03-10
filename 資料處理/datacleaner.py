import pandas as pd
import sqlite3

df=pd.read_excel("資料\資料結構.xlsx")

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0) # 设置打印宽度(**重要**)

dbname="schoolfile.db"
db=sqlite3.connect(dbname)

replacelist={"淡江大學學校財團法人淡江大學":"淡江大學","台灣首府學校財團法人台灣首府大學":"台灣首府大學","明道學校財團法人明道大學":"明道大學",
"慈濟學校財團法人慈濟大學":"慈濟大學","中華大學學校財團法人中華大學":"中華大學","中信學校財團法人中信金融管理學院":"中信金融管理學院",
"馬偕學校財團法人馬偕醫學院":"馬偕醫學院","法鼓學校財團法人法鼓文理學院":"法鼓文理學院","嘉藥學校財團法人嘉南藥理大學":"嘉南藥理大學",
"南臺學校財團法人南臺科技大學":"南台科技大學","台南家專學校財團法人台南應用科技大學":"台南應用科技大學","明新學校財團法人明新科技大學":"明新科技大學",
"大華學校財團法人敏實科技大學":"敏實科技大學","萬能學校財團法人萬能科技大學":"萬能科技大學","正修學校財團法人正修科技大學":"正修科技大學",
"華夏學校財團法人華夏科技大學":"華夏科技大學","健行學校財團法人健行科技大學":"健行科技大學","修平學校財團法人修平科技大學":"修平科技大學",
"中華學校財團法人中華科技大學":"中華科技大學","城市學校財團法人臺北城市科技大學":"臺北城市科技大學","崇右學校財團法人崇右影藝科技大學":"崇右影藝科技大學",
"致理學校財團法人致理科技大學":"致理科技大學","醒吾學校財團法人醒吾科技大學":"醒吾科技大學","光宇學校財團法人元培醫事科技大學":"元培醫事科技大學",
"長庚學校財團法人長庚科技大學":"長庚科技大學","慈濟學校財團法人慈濟科技大學":"慈濟科技大學","美和學校財團法人美和科技大學":"美和科技大學",
"亞東學校財團法人亞東科技大學":"亞東科技大學","廣亞學校財團法人育達科技大學":"育達科技大學","南亞科技學校財團法人南亞技術學院":"南亞技術學院",
"馬偕學校財團法人馬偕醫護管理專科學校":"馬偕醫護管理專科學校"}

# df.to_sql("人工智慧開課學校", db,if_exists="replace" ,index=False)
df2=pd.read_sql(con=db, sql="select 學年度,學校名稱,設立別, AVG(註冊率) AS '註冊率' FROM (select * from '106to110' where 學年度='110') GROUP BY 學校名稱")
df2["學校名稱"].replace(replacelist,inplace=True)
df2.to_sql("110年註冊率", db,if_exists="replace" ,index=False)
df3=pd.read_sql(sql="select * from '人工智慧開課學校' AS t1 LEFT JOIN (SELECT * FROM '110年註冊率') AS t2 ON t1.學校名稱=t2.學校名稱 ", 
con=db)
df3.to_excel("dataforxgb.xlsx",index=False)

