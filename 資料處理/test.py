from itertools import combinations
from collections import Counter
import pandas as pd

##找到最常出現的搭銷組合
# df=pd.read_excel("成功案例.xlsx")

# count_pairs=Counter()

# for row in df['products']:
    
#     row_list=row.split(',')
#     count_pairs.update(Counter(combinations(row_list,2)))

# print(count_pairs.most_common(5))


#===============================
a=['', '0人工智慧作業平台', '21', '1', '1', '1', '', '0人工智慧實務應用', '20', '1', '1', '1', '', '0人工智慧導論', '49', '1', '1', '1', '', 'AC000A自然科學與人工智慧導論', '63', '1', '1', '1', '']

tit=[]
clss=[]
dep=[]
scho=[]
peo=[]
cou=0
for i in a:
    if cou==0:
        cou+=1
    elif cou==1:
        tit.append(i)
        cou+=1
    elif cou==2:
        peo.append(i)
        cou+=1
    elif cou==3:
        clss.append(i)
        cou+=1
    elif cou==4:
        dep.append(i)
        cou+=1
    elif cou==5:
        scho.append(i)
        cou=0


