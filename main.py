import pandas

dog_bite_data = pandas.read_csv("Dog_Bite_Data.csv")

custom_dog_bite_data = {
    "date_of_bite": dog_bite_data['DateOfBite'][:50],
    "age": dog_bite_data['Age'][:50],
    "breed": dog_bite_data['Breed'][:50],
    "gender": dog_bite_data['Gender'][:50]
}

custom_dog_bite_dataframe = pandas.DataFrame(custom_dog_bite_data)
print(custom_dog_bite_dataframe)

# Creates a csv file from the columns I chose
custom_dog_bite_dataframe.to_csv("custom_dog_bite_data.csv")