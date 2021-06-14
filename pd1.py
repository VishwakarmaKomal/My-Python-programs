import pandas as pd
Data=[1,3,4,5,6,2,9]
s=pd.Series(Data)
Index=['a','b','c','d','e','f','g']
si=pd.Series(Data,Index)
print(si)