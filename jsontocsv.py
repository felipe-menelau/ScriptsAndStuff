import pandas
from pandas.io.json import json_normalize

f = open("sites.json", 'r')
#print f.read()

df = pandas.read_json(f.read())

json_normalize(df['my_column'])
df.to_csv("site.csv")

#(pandas.DataFrame(f.read())).to_csv("site.csv")