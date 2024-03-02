# -*- coding: utf-8 -*-
"""WEBSCRAPPING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18EpO9A8s4iRpXfw8RUq_YjREckGKHvvY
"""

from bs4 import BeautifulSoup
import requests

url="https://joecoffeecompany.com/"

page=requests.get(url)

soup=BeautifulSoup(page.text,'html')
print(soup)

title=soup.find('title')
print(title)

print(title.text)