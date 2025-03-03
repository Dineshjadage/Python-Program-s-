"""program to demonstrate pandas"""

import pandas as pd

#DataFrame
p={"id":[1,2],
   "name":["Jack","Rose"],
   "degree":["MS","PHD"],
   "sal":[20000,30000]}

df=pd.DataFrame(p)
print(df)

#Series
s=pd.series([1,2,3],index=['a','b','c'])
print(s)
print(s['c'])

"""output:
   id  name degree    sal
0   1  Jack     MS  20000
1   2  Rose    PHD  30000
a    1
b    2
c    3
dtype: int64
3"""
