import pandas

car_data = pandas.read_csv("car_data.csv")
weather_data = pandas.read_csv("weather_data.csv")

car_data_dict = car_data.to_dict()
weather_data_dict = weather_data.to_dict()

print(car_data_dict)
print('\n')
print(weather_data_dict)

print(car_data['Car Model'].to_list())

# Create a dataframe from scratch
data_dict = {
    "students": ['Amy', 'James', 'Angela'],
    "scores": [80, 85, 90]
}

my_df = pandas.DataFrame(data_dict)
print(my_df)