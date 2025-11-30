import pandas as pd
import os

#create a sample dataframe with column name

data = {'name': ['alice', 'bob', 'charlie'],
        'age': [25, 30, 35],
        'city': ['newyork', 'los angles', 'chicag']
        }

df = pd.DataFrame(data)

## Adding new row to df for V2
new_row_loc = {'name': 'gf1', 'age':20, 'city': 'blr'}
df.loc[len(df.index)] = new_row_loc

## Adding new row to df for V3
new_row_loc2 = {'name': 'GF2', 'age':30, 'city': 'hyd'}
df.loc[len(df.index)] = new_row_loc2


# Adding new row to df for V4
new_row_loc3 = {'name': 'GF3', 'age':30, 'city': 'chennai'}
df.loc[len(df.index)] = new_row_loc3

#Ensure the "data" directry exists at the root level

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

#define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

#save teh dataframe to a csv file including column names

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")
