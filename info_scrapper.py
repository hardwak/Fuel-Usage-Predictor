import os

import kaggle
import pandas as pd
import requests


def get_datasets():
    return get_fuel_consumption(), get_sold_cars_data(), get_temperature_data()


def get_temperature_data():
    dataset_path = 'sarahquesnelle/canada-data'
    filename = 'datasets/Canada_Temperature_Data.csv'

    data = download_dataset_from_kaggle(filename, dataset_path)

    # reformatting data and storing annual values
    annual_mean_temperatures = data.groupby('Year').agg({
        'Tm': 'mean',
        'S': 'sum',
        'P': 'sum'
    }).reset_index()

    annual_mean_temperatures.columns = ['Year', 'Mean Temperature', 'Total Snowfall', 'Total Precipitation']

    return annual_mean_temperatures


def get_sold_cars_data():
    # gets amount of sold cars between
    url = ("https://www150.statcan.gc.ca/t1/tbl1/en/dtl!downloadDbLoadingData-nonTraduit.action?pid=2010000101"
           "&latestN=0&startDate=19460101&endDate=20231201&csvLocale=en&selectedMembers=%5B%5B1%5D%2C%5B1%5D%2C%5B1"
           "%5D%2C%5B1%2C2%5D%2C%5B1%5D%5D&checkedLevels=")
    filename = "datasets/sold_cars_units_1946-2023.csv"

    if not os.path.isfile(filename):
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print("File downloaded successfully!")
        else:
            print("Failed to retrieve the file. Status code:", response.status_code)

    data = pd.read_csv(filename)

    # reformatting data and storing annual values
    data['Year'] = data['REF_DATE'].str.split('-').str[0]
    data['Year'] = pd.to_numeric(data['Year'])
    annual_values = data.groupby('Year')['VALUE'].sum().reset_index()

    return annual_values


def get_fuel_consumption():
    dataset_path = 'ahmettyilmazz/fuel-consumption'
    filename = 'datasets/Fuel_Consumption_2000-2022.csv'

    data = download_dataset_from_kaggle(filename, dataset_path)

    # reformatting data in columns
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].str.upper()
    data['VEHICLE CLASS'] = data['VEHICLE CLASS'].str.replace(': ', ' - ')

    return data


def get_demographics():
    url = 'https://en.wikipedia.org/wiki/Demographics_of_Canada'
    filename = 'datasets/Demographics_of_Canada.csv'

    if not os.path.isfile(filename):
        dfs = pd.read_html(url, header=0)

        for df in dfs:
            if 'Average population (on July 1)' in df.columns:
                df = df.iloc[:, :5]
                df.columns = ['Year', 'Average Population', 'Live Births', 'Deaths', 'Natural Change']

                df.to_csv(filename, index=False)
                break

    return pd.read_csv(filename)


def download_dataset_from_kaggle(filename, dataset_path):
    if not os.path.isfile(filename):
        print(f'Downloading csv dataset from Kaggle...')
        kaggle.api.dataset_download_files(dataset_path, path='datasets', unzip=True)

    return pd.read_csv(filename)
