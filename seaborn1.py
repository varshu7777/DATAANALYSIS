# -*- coding: utf-8 -*-
"""SEABORN1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GwQTj31-svPymo6YUYw25sVhjxGulcpE
"""

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.scatterplot(x="total_bill", y="tip", data=tips,label="varshu")
plt.title("Scatter plot of Total Bills vs. Tips")
plt.xlabel("Total  Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.barplot(x="day", y="total_bill", data=tips,label="varshu")
plt.title("Average total bill in a day")
plt.xlabel("Day of the week ")
plt.ylabel("Average totel bill")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.boxplot(x="day",  y="total_bill", data=tips)
plt.title("Distribution of total bill by day")
plt.xlabel("Day of the week ")
plt.ylabel("total bill ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.violinplot(x="day",  y="total_bill", data=tips)
plt.title("Distribution of total bill by day")
plt.xlabel("Day of the week ")
plt.ylabel("total bill ($)")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
a=pd.read_csv("/content/drive/MyDrive/DATASET/grades_withnulls.csv")
b=sns.lineplot(x="SEM1",y="SEM2",data=a)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
co=iris.corr()
sns.heatmap(co, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.jointplot(x="total_bill", y="tip", data=tips,label="varshu")
plt.title("Joint Distribution plot of Total Bills vs. Tips")
plt.xlabel("Total  Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.countplot(x="day",data=tips)
plt.title("Joint Distribution plot of Total Bills vs. Tips")
plt.xlabel("Day")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips)
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.title("Linear Regression plot of Total Bills vs. Tips")
plt.xlabel("Total  Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
titanic=sns.load_dataset("titanic")
print(titanic)
g=sns.FacetGrid(titanic,col="class")
g.map(sns.histplot,"age")
plt.subplots_adjust(top=0.8)
g.fig.suptitle("Age Distribution by passenger class")
plt.show()