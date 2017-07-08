#encoding=utf8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
#创建DataFrame
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#通过字典创建DataFrame
f2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
print(f2)

#探索数据

print("前五行：",df.head())
print("后三行：",df.tail(3))
print("index: ",df.index)
print("columns: ",df.columns)
print("values: ",df.values)
print("describe: ",df.describe())
print("转置：",df.T)
print("按照axis排列：",df.sort_index(axis=0, ascending=False))
print("按照某列排序：",df.sort_values(by='B'))
