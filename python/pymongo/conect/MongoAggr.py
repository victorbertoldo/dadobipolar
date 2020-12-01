#!python
from pymongo import MongoClient
import pandas as pd
import openpyxl
import datetime
from bson.son import SON

# Conectando no mongo

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://<ipservidor>:27017/")

# Access database
mydatabase = client['mdfe']

# Access collection of the database
mycollection = mydatabase['mdfeProcessado']

print(mycollection)

pipeline = [
    {"$match": {"referenciaMDFe":"10/2020"}},
    {"$group":{
        "_id":{ "ufEmissor": "$ufEmissor"},
        "count": {"$sum": 1}
        }
    }]

docs = mycollection.aggregate(pipeline)

df = pd.DataFrame.from_dict(pd.json_normalize(docs))
print(df.columns)
print(df.head())
df.rename(columns={'_id.ufEmissor': 'ufEmissor', 'count':'QtdMDFe'}, inplace=True)
print(df.columns)


obj = {'ufEmissor': [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53, 99],
       'UF': ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ',
        'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF', 'EX']}

uf = pd.DataFrame(data=obj)

dfAggrUF = pd.merge(uf, df, on=['ufEmissor'], how='inner')

print(dfAggrUF.head())

datasetANTT = dfAggrUF.sort_values('QtdMDFe', ascending=False).set_index('ufEmissor')

print(datasetANTT)

datasetANTT.to_excel(r'D:\ANTT\Aggr\datasetANTT.xlsx', index=False)