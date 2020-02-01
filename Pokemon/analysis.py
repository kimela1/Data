import pandas as pd

df = pd.read_csv('C:/Users/Elaine/Desktop/pokemon_data.csv')
#df_xlsx = pd.read_excel('C:/Users/Elaine/Desktop/pokemon_data.xlsx')

# Read headers
df.columns

# Read each column
df[['Name', 'Type 1', 'HP']]

# Read each row
df.iloc[1:4]

# Read a specific location (R, C)
df.iloc[2,1]

# Filtering data
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True)
new_df
new_df.to_csv('filtered.csv')