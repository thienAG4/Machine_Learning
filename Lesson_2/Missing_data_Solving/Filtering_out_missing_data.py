from numpy import nan as na
import pandas as pd
data=pd.DataFrame([[1,2,3],[1,na,na],[na,na,na],[na,5.6,7]])
print(data)
print("-"*10)
cleaned=data.dropna()
print(cleaned)
print("-"*10)
cleaned2=data.dropna(how="all") #van giu cac dong NaN ma co gia tri, theo dieu kien how
print(cleaned2)

#Filter la dep no khoi dataset, bo no ra khoi 
