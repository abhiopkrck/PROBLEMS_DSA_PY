import pandas as pd

calaories={
    "day1":400,
    "day2":300,
    "day3":200,
}

df=pd.DataFrame(calaories,index=["day1","day2","day3"])

print(df)