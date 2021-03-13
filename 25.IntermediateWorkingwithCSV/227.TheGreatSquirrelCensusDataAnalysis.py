import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count())

new_data = {}

# count_black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
# count_red = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
# count_grey = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
count_black = len(data[data["Primary Fur Color"] == "Black"])
count_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_grey = len(data[data["Primary Fur Color"] == "Gray"])


new_data = {
    "Fur Color": ["black", "red", "gray"],
    "Count": [count_black, count_red, count_grey]
}
print(new_data)

data_csv = pandas.DataFrame(new_data)
data_csv.to_csv("count_squirrel.csv")
