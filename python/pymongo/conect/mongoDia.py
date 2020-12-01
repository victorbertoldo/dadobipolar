#!python
from pymongo import MongoClient
import pandas as pd
import openpyxl
import datetime

# Conectando no mongo

client = MongoClient('<ipservidor>', 27017)
db = client.get_database('mdfe')
collection = db.get_collection('mdfeProcessado')

# Range de datas
datas = pd.date_range('20201001', periods = 31, freq="D")

print(datas)

for dt in datas:
    dia = dt.strftime("%Y-%m-%d")

    docs = collection.find({'dataHoraEmissao': dia})
    df = pd.DataFrame(list(docs))
    print(df.columns)
    print(df.head())



    obj = {'ufEmissor': [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53, 99],
       'UF': ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ',
        'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF', 'EX']}

    uf = pd.DataFrame(data=obj)

    aggrUf = df.groupby(['ufEmissor','dataHoraEmissao'])['chaveMDFe'].nunique()

    aggrUf = aggrUf.reset_index()

    print(aggrUf.head())

    dfAggrUF = pd.merge(uf, aggrUf, on=['ufEmissor'], how='inner')

    print(dfAggrUF.head())

    datasetANTT = dfAggrUF.sort_values('chaveMDFe', ascending=False).set_index('ufEmissor')

    datasetANTT.columns = ['UF', 'Data', 'Qtd_MDFe']

    print(datasetANTT.head())

    datasetANTT.to_excel(r'D:\ANTT\datasetANTT_%s.xlsx' % (dia), index=False)
