# -*- coding: utf-8 -*-
"""Countung.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13q24EP7jpcuXaD2xO4E9nljMGLHFTGyN
"""

a = input()
asplit = a.split()
count = 0
for i in range(len(asplit)):
    if(int(asplit[i])<60):
      count+=1
print(count)