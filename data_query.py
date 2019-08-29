'''
create data table based on query from substance property database
'''

from produce_data import main

prop = 'log Kow'
df = main(prop)
df.dropna(axis = 0, inplace = True)
df = df[['SMILES', 'value']]
df.rename(columns = {'SMILES': 'smiles', 'value' : prop})
df.to_csv(r'validation_data\SOLUTIONS_%s.csv' % prop)
