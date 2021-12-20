# with open("./weather_data.csv") as data:
#     list_of_data = data.readlines()
#     data_list =[i.strip() for i in list_of_data]
#     print(data_list)

# import csv
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = [int(row[1]) for row in data if row[1]!="temp" ]

# this is inbuilt  library many stuff are required for fetching the
# single column what about many column here the pandas come into picture

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# series is like a list  of the particular column specified
# dataframe is the equivalent to the each excel sheet
# print(data.columns)
# print(data.index)
# file and format convertion

# for data frame
# data_dict = data.to_dict()
# print(data_dict)
# data_dict = {
#     'day': ['mon', 'tue', 'wednes'], 'digit': [16, 37, 90]}
# dataframe = pandas.DataFrame(data=data_dict)
# print(dataframe)

# series object
to_list = data['temp'].to_list()
# print(to_list)
list_of_temp = data['temp'].to_list()

# print(data['temp'].mean())
#
# print(data['temp'].max())
# print(data.temp.max())

# print(data[data.day == "Monday"])

# print(data[data.temp==max(data.temp.to_list())])
# print(list(data[data.temp == data.temp.max()].condition)[0])
######################
c = int(data[data.temp == data.temp.max()].temp)

fran = ((c / 100) * 180) + 32
print(fran)

# c= data[data.temp==data.temp.min()]
# print(c)
# how to create the data frame from scrach
# by pandas
data_dict = {
    "san": [90, 99, 98],
    'vis': [99, 93, 100]
}
data = pandas.DataFrame(data_dict)
data.to_csv("./score.csv")
