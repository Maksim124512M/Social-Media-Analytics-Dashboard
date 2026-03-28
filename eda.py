import pandas as pd

df = pd.read_csv('data/youtube.csv')

# General information
print(f'First 5 dataframe: {df.head()}')
print(f'Last 5 dataframe: {df.tail()}')
print(f'Info about dataframe: {df.info()}')
print(f'Dataframe description: {df.describe()}')

# Dublicates and NaN's
print(f'NaN values in dataframe: \n {df.isna().sum()}')
print(f'Duplicates in dataframe: \n {df.duplicated().sum()}')

print(df[df['likes'] >= 57527])