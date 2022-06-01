import pandas

car_data = pandas.read_csv("car_data.csv")
weather_data = pandas.read_csv("weather_data.csv")

print(car_data)
print('\n')
print(weather_data)
print('\n')

# Convert to dictionaries
car_data_dict = car_data.to_dict()
weather_data_dict = weather_data.to_dict()

print(car_data_dict)
print('\n')
print(weather_data_dict)
print('\n')

# Convert to lists
print(car_data['Car Make'].to_list())
print('\n')
print(weather_data['day'].to_list())
print('\n')

# Create a dataframe
some_data = {
    "athletes": ['Tom Brady', 'Kobe Bryant', 'Steph Curry'],
    "teams": ['Tampa Bay Buccaneers', 'LA Lakers', 'Golden State Warriors']
}

my_df = pandas.DataFrame(some_data)
print(my_df)
print('\n')

# Creates a new csv file with your provided data
my_df.to_csv("athlete_data.csv")
