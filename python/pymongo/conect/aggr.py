import pandas as pd
import glob

path = r'D:\ANTT'
all_files = glob.glob(path + "/*.xlsx")

li = []

for filename in all_files:
    df = pd.read_excel(filename, 'Sheet1')
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)

DataSet = frame.groupby(['UF'], as_index=False)['Qtd_MDFe'].sum().sort_values('Qtd_MDFe', ascending=False)
print(DataSet)

DataSet.to_excel(r'D:\ANTT\Aggr\datasetANTT.xlsx', index=False)