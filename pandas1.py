# -*- coding: utf-8 -*-
"""PANDAS1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WaommDuM3yq6p-34D9Nw8kiNx8S-HDtu
"""

import pandas as pd
a=["varshini","hema","likitha","sneha","gayatri","bhargavi"]
r=pd.Series(a,index=[67,43,44,89,34,45])
print(r)

df=pd.read_csv("/content/drive/MyDrive/DATASET/diabetcsv.csv")
print(df)

df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv",sep=" ")
print(df)

df=pd.read_excel("/content/drive/MyDrive/DATASET/sugar.xlsx")
print(df)

df=pd.read_excel("/content/drive/MyDrive/DATASET/sugar.xlsx",sheet_name=0)
print(df)

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
print(df.head())
print(df.tail(n=10))

import pandas as pd
df=pd.read_excel("/content/drive/MyDrive/DATASET/sugar.xlsx")
print(df.describe)

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
print(df.describe().T)

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
print(df.shape) #gets no of rows and columns
print(df.shape[0]) #get noof rows only
print(df.shape[1]) #gets noof columns only

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
print(df.columns)
l=list(df.columns)
print(l)

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
df1=df.copy()
df1.loc[2:5,'SEM1']=None
df1.head(7)

df1.isnull().head(7)

df1.isnull().tail(7)

print(df1.isnull().sum())

print(df['SEM1'])

print(df1[['SEM1','Names']])

print(df[df.index==1]) #printing one row

print(df[df.index.isin(range(2,5))]) #printing multiple row

print(df1.loc[1]) #printing one row as series

print(df1.loc[6:11])

df1.loc[2:5,'SEM1']==None
print(df1)

df1.loc[[10,2,7]]

df1.loc[10:15,['Names','Grade',]]

df1.iloc[10:14,:3]

df1.loc[:7,["Names"]]

df1.loc[df['Names']=='Rajesh']

df[df.Grade=='A']
df[df.SEM2==10]

df.loc[df['SEM1'] >9.8,['Names']]

df2=df1.copy()
#df2=df2.dropna()
df2

df2.dropna(inplace=True,axis=1)
df2

df2.dropna(inplace=True,how='all')
df2

mv=df1['SEM1'].mean()
dfn=df1.fillna(mv)
print(dfn)