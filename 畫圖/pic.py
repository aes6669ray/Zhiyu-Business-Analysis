import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0) # 设置打印宽度(**重要**)
	
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

df=pd.read_excel("成功案例.xlsx")
cond=df["purpose"]=="上課"
df=df[cond]

labels=df["subtitle"]
result = df.groupby('subtitle').size().reset_index(name='count')


plt.figure(figsize=(6,9))

separated = (.1,0,0)

plt.title("課程內容", {"fontsize" : 18})
plt.pie(result["count"],                           # 數值
        labels = result["subtitle"],                # 標籤
        autopct = "%1.1f%%",
        explode=separated,            # 將數值百分比並留到小數點一位         
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=True)
plt.axis('equal') 

plt.legend(loc = "best") 
plt.show()
plt.savefig("課程內容.jpg")

