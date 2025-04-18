import pandas as pd

df = pd.read_csv('./publications.csv')
src =['Under Review','https://ieeexplore.ieee.org/abstract/document/10565868','https://ieeexplore.ieee.org/abstract/document/10138182']

j = df['journal'].tolist()
c= df['conference'].tolist()
ds ={'paper':j,'source':src}
ds1 ={'paper':c}
ds = pd.DataFrame(ds)
ds1= pd.DataFrame(ds1)
ds.to_csv('./doc/journal.csv',index=False)
ds1.to_csv('./doc/conference.csv',index=False)
