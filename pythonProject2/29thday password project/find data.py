import pandas
data = pandas.read_csv('data.csv')
web = input("enter the website name").strip().lower()
print(data[data.website==web])