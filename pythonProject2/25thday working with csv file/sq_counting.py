import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
list_color = list(data['Primary Fur Color'])
print(list_color)

data_dict = {
    'Fur Color': ['grey', 'cinnamon', 'black'],
    'count': [list_color.count("Gray"),
              list_color.count("Cinnamon"),
              list_color.count("Black")]
}
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("./sq_count.csv")
# alternative
# grey = len(list(data[data['Primary Fur Color'] == "Gray"]))
# print(grey)