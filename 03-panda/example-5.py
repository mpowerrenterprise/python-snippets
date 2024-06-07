import pandas as pd

df = pd.read_excel("pokemon_data.xlsx") #read excel files

#print(df['Name']) #print specific data
#print(df['Name'][0:5]) #print 0-5

print(df.describe())

