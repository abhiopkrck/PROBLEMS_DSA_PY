import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pandas.DataFrame(mydataset)
print(df.loc[0])
print(df.loc[[0,1]])
print(df)