import pandas as pd

df=pd.read_excel("成功案例.xlsx")

cli=[]
buy=[]
for n,i in enumerate(df["client"]):
    cli.append(i)
    buy.append(df.iloc[n,1].split(","))

dic={"client":cli,"product":buy,"education":list(df["education"])}
df2=pd.DataFrame(dic)
df2=df2.explode("product").reset_index(drop=True)
df2.to_excel("產品面向.xlsx")