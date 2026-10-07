import pandas as pd

a=[2,3,4]

df=pd.Series(a,index=["x","y","z"])

print(df)
print(df["y"])
