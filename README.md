# MSiD Project: Predicting Fuel Consumption

## Overview

This project aims to predict the fuel consumption of cars based on various factors. The analysis is conducted on datasets containing information about car specifications, fuel types, weather conditions, and population demographics in Canada. The objective is to create a model that accurately predicts fuel consumption.

## Problem Description

The primary problem addressed in this project is predicting car fuel consumption based on other factors such as engine characteristics, type of fuel used, weather conditions, and population data. The goal is to explore these relationships and build a model capable of making reliable predictions about car fuel consumption.

## Datasets Used

Four datasets were used in this project, all pertaining to Canada:

1. **Car Specifications and Fuel Consumption**: Contains information on car production year, make, model, engine characteristics, transmission, fuel type, and fuel consumption indicators.
   - Source: [Kaggle](https://www.kaggle.com/datasets/ahmettyilmazz/fuel-consumption/code)

2. **Weather Data**: Contains monthly average temperatures and precipitation levels.
   - Source: [Kaggle](https://www.kaggle.com/datasets/sarahquesnelle/canada-data/data)

3. **Car Production Data**: Contains the number of cars produced each year.
   - Source: [Statistics Canada](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010000101)

4. **Population Data**: Contains annual population data for Canada.
   - Source: [Wikipedia](https://en.wikipedia.org/wiki/Demographics_of_Canada)

## Data Processing

### Car Specifications and Fuel Consumption

- Cleaned to standardize values (e.g., car make written in different cases).
- Converted fuel type abbreviations to full names for clarity.

### Weather Data

- Aggregated to provide yearly averages for temperature, total precipitation, and snowfall.

### Car Production Data

- Filtered to retain only relevant information about the number of cars produced annually.

### Population Data

- Scraped from Wikipedia and processed to provide annual population figures.

## Analysis and Modeling

### Data Analysis

Relationships were explored between:

- Engine capacity, number of cylinders, fuel type, and fuel consumption.
- Weather conditions, population, and car production.

### Predictive Models

Five different models were trained and evaluated:

1. **Linear Regression**
2. **Generalized Linear Model (GLM)**
3. **XGBoost**
4. **Scaled Support Vector Machine (SVM)**
5. **Random Forest**

The training period was from 2000 to 2017, ensuring all required data was available. Unnecessary columns like car make, model, and transmission type were excluded from training to focus on relevant features.

### Model Evaluation

The models were evaluated using the following metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

The XGBoost model outperformed the others with the highest R² score and lowest error rates, indicating its superior ability to predict fuel consumption accurately.

## Conclusion

The project successfully developed a model for predicting car fuel consumption using a combination of car specifications, weather data, and demographic information. The XGBoost model was identified as the most effective predictor.
