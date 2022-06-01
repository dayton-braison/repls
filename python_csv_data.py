import csv

with open("weather_data.csv") as weather_data_file:
    weather_data = csv.reader(weather_data_file)

    headings = next(weather_data)
    temperatures = []
    for row in weather_data:
        print(f'{row}')
        temperatures.append(row[1])
    print(f'The list of temperatures: {temperatures}')

print('\n\n')

with open("car_data.csv") as car_data_file:
    car_data = csv.reader(car_data_file)
    for row in car_data:
        print(f'{row}')

