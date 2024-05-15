import info_scrapper as scr
import dataset_tools as dttl

import seaborn as sns
import matplotlib.pyplot as plt

cars_and_fuel_con, sold_cars_data, mean_temp_data = scr.get_datasets()
print(cars_and_fuel_con)
print(sold_cars_data)
print(mean_temp_data)


# SOLD CARS UNITS PLOT
start_year = 2000
end_year = 2023

sns.set_style("whitegrid")

sold_cars_filtered = dttl.filter_by_year(sold_cars_data, start_year, end_year)

plt.figure(figsize=(10, 5))
sold_cars_plot = sns.barplot(x='Year', y='VALUE', data=sold_cars_filtered, palette='crest')

plt.title('Amount of cars sold by Year')
plt.xlabel('Year')
plt.ylabel('Amount')

plt.tight_layout()
plt.savefig(f'plots/Amount of cars sold by Year {start_year}-{end_year}.png')
plt.show()


# MEAN TEMPERATURE VALUES
start_year = 2000
end_year = 2017

mean_temp_filtered = dttl.filter_by_year(mean_temp_data, start_year, end_year)
mean_temp_plot = sns.relplot(x='Year', y='Mean Temperature', data=mean_temp_filtered, kind='line', aspect=1.5)

plt.title('Mean temperatures by Year')
plt.xlabel('Year')
plt.ylabel('Temperature')

plt.xticks(rotation=45)
plt.gca().set_xticks(mean_temp_filtered['Year'])

plt.tight_layout()
plt.savefig(f'plots/Mean Temperatures {start_year}-{end_year}.png')
plt.show()


# CARS AND FUEL CONSUMPTION ANALYSIS

# Models plot
plt.figure(figsize=(10, 4))
#car_models_plot = sns.countplot(y='MAKE', data=cars_and_fuel_con, order=sorted(cars_and_fuel_con['MAKE'].unique()))
car_models_plot = sns.countplot(y='MAKE',
                                data=cars_and_fuel_con,
                                order=cars_and_fuel_con['MAKE'].value_counts().head(10).index)
plt.title('10 most common car models')
plt.xlabel('Amount')
plt.ylabel('Model')

plt.tight_layout()
plt.savefig('plots/10 most common car models.png')
plt.show()

# Engine size with fuel consumption
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ENGINE SIZE', y='FUEL CONSUMPTION', data=cars_and_fuel_con)

plt.title('Dependency between engine size and fuel consumption')
plt.xlabel('Engine size')
plt.ylabel('Fuel Consumption (L/100 km)')

plt.tight_layout()
plt.savefig('plots/Dependency between engine size and fuel consumption.png')
plt.show()

# Fuel consumption with emissions
sns.scatterplot(x='FUEL CONSUMPTION', y='EMISSIONS', data=cars_and_fuel_con)
plt.title('Fuel consumption VS Emissions')
plt.show()



# Yearly emissions
yearly_emissions = cars_and_fuel_con.groupby('YEAR')['EMISSIONS'].mean().reset_index()
yearly_emissions.columns = ['Year', 'Mean Emissions']

yearly_emissions_plot = sns.relplot(x='Year', y='Mean Emissions', data=yearly_emissions, kind='line', aspect=1.5)

plt.title('Cars Mean CO2 Emissions (g/km) by Year')

plt.tight_layout()
plt.savefig('plots/Cars Mean CO2 Emissions (g km) by Year.png')
plt.show()


# DEPENDENCIES BETWEEN DATASETS
# # Dependency between car emissions and mean temperature
# yearly_emissions = dttl.filter_by_year(yearly_emissions, 2000, 2017)
# X = yearly_emissions['Total Emissions']
# Y = mean_temp_filtered['Mean Temperature']
#
# emissions_temp_plot = sns.relplot(x=X, y=Y)
#
# plt.title("Dependency between car emissions and mean temperature")
# plt.tight_layout()
# plt.savefig('plots/Dependency between car emissions and mean temperature.png')
#
# plt.show()
#
# # Dependency between car emissions and amount of sold cars
# start_year = 2000
# end_year = 2022
# yearly_emissions = dttl.filter_by_year(yearly_emissions, start_year, end_year)
# sold_cars_filtered = dttl.filter_by_year(sold_cars_data, start_year, end_year)
# X = yearly_emissions['Total Emissions']
# Y = sold_cars_filtered['VALUE']
#
# emissions_units_plot = sns.relplot(x=X, y=Y)
#
# plt.ylabel('Amount of sold cars')
#
# plt.title("Dependency between car emissions and amount of sold cars")
# plt.tight_layout()
# plt.savefig('plots/Dependency between car emissions and amount of sold cars.png')
#
# plt.show()

# Dependency between amount of car emissions and mean temperature
yearly_emissions = cars_and_fuel_con.groupby('YEAR')['EMISSIONS'].mean().reset_index()
yearly_emissions.columns = ['Year', 'Mean Emissions']

X = yearly_emissions['Mean Emissions'] * sold_cars_filtered['VALUE']
Y = mean_temp_filtered['Mean Temperature']

mean_emissions_temp_plot = sns.relplot(x=X, y=Y)

plt.xlabel("Mean emissions by one car")

plt.title("Mean car emissions and mean temperature")
plt.tight_layout()
plt.savefig('plots/Mean car emissions and mean temperature.png')

plt.show()

# Dependency between amount of mean car emissions and amount of cars produced
X = yearly_emissions['Mean Emissions']
Y = sold_cars_filtered['VALUE']

mean_emissions_cars_sold_plot = sns.relplot(x=X, y=Y)

plt.xlabel("Mean emissions by one car")
plt.ylabel("Amount of cars sold")

plt.title("Mean car emissions VS Sold cars")
plt.tight_layout()
plt.savefig('plots/Mean car emissions VS Sold cars.png')

plt.show()

# Dependency between mean temperature and amount of cars produced
X = mean_temp_filtered['Mean Temperature']
Y = sold_cars_filtered['VALUE']

mean_temp_cars_sold_plot = sns.relplot(x=X, y=Y)

plt.xlabel("Mean temperature")
plt.ylabel("Amount of cars sold")

plt.title("Mean temperature VS Sold cars")
plt.tight_layout()
plt.savefig('plots/Mean temperature VS Sold cars.png')

plt.show()

# Dependency between mean fuel consumption and amount of cars produced
yearly_fuel_consumption = cars_and_fuel_con.groupby('YEAR')['FUEL CONSUMPTION'].mean().reset_index()
yearly_fuel_consumption.columns = ['Year', 'Fuel consumption']

X = yearly_fuel_consumption['Fuel consumption']
Y = sold_cars_filtered['VALUE']

mean_fuel_cons_cars_sold = sns.relplot(x=X, y=Y)

plt.ylabel("Amount of cars sold")

plt.title("Mean Fuel Consumption VS Sold cars")
plt.tight_layout()
plt.savefig('plots/Mean Fuel Consumption VS Sold cars.png')

plt.show()

# Emissions made in every year
X = yearly_emissions['Year']
Y = yearly_emissions['Mean Emissions'] * sold_cars_filtered['VALUE']

emissions_amount_cons_cars_sold = sns.relplot(x=X, y=Y)

plt.ylabel("Amount of emissions")

plt.title("Amount of emissions in every year")
plt.tight_layout()
plt.savefig('plots/Amount of emissions in every year.png')

plt.show()

# Emissions made vs mean temperature
Y = yearly_emissions['Mean Emissions'] * sold_cars_filtered['VALUE']
X = mean_temp_filtered['Mean Temperature']

emissions_amount_mean_temp = sns.relplot(x=X, y=Y)

plt.ylabel("Emissions amount")

plt.title("Amount of emissions vs Mean Temperature")
plt.tight_layout()
plt.savefig('plots/Amount of emissions vs Mean Temperature.png')

plt.show()


