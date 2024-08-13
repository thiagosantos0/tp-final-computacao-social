

# Passing the 'rodada' column from a csv to another, based on the 'id' column

import pandas as pd

df1 = pd.read_csv('./brzao2023_2.csv')
rodada = df1['rodada']


df2 = pd.read_csv('./brzao2023.csv')
df2['rodada'] = rodada

# escrevendo o arquivo
df2.to_csv('brzao2023_.csv', index=False)

