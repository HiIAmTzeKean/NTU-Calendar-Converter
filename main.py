import pandas as pd

df = pd.read_html(open("try.html"),header=0)
print(df.columns)
# print(df['Course'])