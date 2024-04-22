import pandas as pd
import os
import kaggle

file = 'Fuel_Consumption_2000-2022.csv'
dataset_path = 'ahmettyilmazz/fuel-consumption'

if not os.path.isfile(file):
    print(f'Downloading {file} from Kaggle...')
    kaggle.api.dataset_download_files(dataset_path, path='.', unzip=True)
else:
    print(f'File {file} already exists')

data = pd.read_csv(file)

#https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption/download?datasetVersionNumber=1
#data = pd.read_csv('Fuel_Consumption_2000-2022.csv')

for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = data[col].str.upper()
data['VEHICLE CLASS'] = data['VEHICLE CLASS'].str.replace(': ', ' - ')
#
# data.to_csv('Fuel_Consumption_2000-2022_Updated.csv', index=False)

pd.set_option('display.max_columns', None)
print(data.head(10))

unique_values = data['ENGINE SIZE'].unique()

print(unique_values)
