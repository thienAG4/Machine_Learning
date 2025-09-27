#Khi nao nen drop, khi nao filling? Khi drop qua nhiu r, k du de drop nua

from numpy import nan as na
import pandas as pd

data=pd.DataFrame([[1,2,3],[1,na,na],[na,na,na],[na,5.6,7],[8,6,7],[10,5.6,7],[9,5.6,8],[7,5.6,7],[na,na,na]])
print(data)
print("-"*10)

cleaned=data.fillna(data.mean()) #median la trung vi, mean la trung binh
print(cleaned)