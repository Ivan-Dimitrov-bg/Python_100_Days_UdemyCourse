import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

data_list = data["temp"].to_list()
print(data_dict)
print(sum(data_list)/len(data_list))

# average
print(data["temp"].mean())
# max
print(data["temp"].max())
print(data.temp.max())

# Get Data in Row
print(data[data["day"] == "Monday"])

# Find the day with high temp
print(data[data.temp == data.temp.max()])

#extract the valuy from one colum with condition
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp) * 9/5 + 32
print(monday_temp)

# Create Data frame
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")