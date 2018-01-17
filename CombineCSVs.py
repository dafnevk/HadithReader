import pandas as pd
import os

csv_dir_in = 'newCSV'
csv_dir_out = 'csv_output'

df_out = pd.DataFrame()

for fn in os.listdir(csv_dir_in):
    print(fn)
    data = pd.read_csv(os.path.join(csv_dir_in, fn), sep='\t', header=None, encoding='utf-8')
    data.columns = ['hadithID', 'arIsnad', 'arMatn', 'arHadith', 'enHadith']
    data[['collection', 'book', 'hadithNr']] = data['hadithID'].str.extract('([a-z]*)([0-9]*)\_([0-9]*)', expand=True)
    data.to_csv(os.path.join(csv_dir_out, fn), index=False, encoding='utf-8')
    df_out = df_out.append(data)
    
df_out.to_csv(os.path.join(csv_dir_out, '0_combined.csv'), index=False, encoding='utf-8')


