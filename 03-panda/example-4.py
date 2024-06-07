import pandas as pd
#load txt file and delimiate by \t
df = pd.read_csv("pokemon_data.txt",delimiter = '\t') # by tab 
print(df.columns) #print all the columns
