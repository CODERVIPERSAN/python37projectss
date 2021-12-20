# todo-- list comprehension and dictionary comprehension
import pandas

# numbers = [1,2,3]
# new_lis = [i+1 for i in numbers]
# print(new_lis)

# ##############################################################
# interactive coding exercise
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)
# ###############################################################
result = [n for n in numbers if n % 2 == 0]
# print(result)
# ################################################################
with open("./file1.txt") as file:
    file1_list = [i.strip() for i in file.readlines()]
with open("./file2.txt") as file:
    file2_list = [i.strip() for i in file.readlines()]
# print(file1_list,file2_list)
common_list = [int(n) for n in file1_list if n in file2_list]
# print(list(set(common_list)))
#############################################################
# dictionary comprehension
# new_dict ={new_key:new value  for items in list}
# ne_dict ={items:int(items) for items in file1_list}
# print(ne_dict)
# ###############################################
# dictionary comprehension using the dict
# new_dict={new_key:new_value for key,value in existing_dict.items() if test }
# ########################################################
# interactive coding exercise
import re

sentence = "What is the Airspeed Velocity of an Unladen Swaloow? the answer : very large velocity that cant be imagined "
words = re.findall("\w*\S\w", sentence)
# print(words)
# print(words)
word_frequency = {word: len(word) for word in words}
# print(word_frequency)
#############################################
# INTERACTIVE coding exercise
weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 22,
    "sunday": 24
}
# weather_f = {day: round((c / 100) * 180 + 32,1) for day, c in weather_c.items()}
# print(weather_f)
#####################################################
# pandas data frame can be samely treated as dictionary
# create the dataframe
data_dict = {'day': weather_c.keys(), 'temp': weather_c.values()}

data = pandas.DataFrame(data_dict)

# print(data.day[0])
# for i in data.iterrows():
# print(i)
# for key,values in data.items():
#     if key=='day':
#         for i in range(7):
#             if data['day'][i]=='monday':
#                 print(data['temp'][i])
lis = [data.temp[i] for i in data.index]
maxi =max(lis)
# print(maxi)
# for index, row in data.iterrows():
#     if row.temp ==maxi:
#         print(row.day)

index = list(data.temp).index(max(list(data.temp)))
# print(data.day[index])

#############################################################
# todo. create the dictionary in this format {key:value,key:value}
# day 30 exceptional handling
endgame = False
while not endgame:
    try:
        user = input("enter a word").strip().upper()
        if user.isalpha():
            endgame = True
        else:
            raise ValueError("please enter the valid input")
    except ValueError:
        print("you have enter wrong input ")
        pass

user_letter_list = list(user)


dataframe = pandas.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")

# final = [list(dataframe.code)[list(dataframe.letter).index(i)] for i in user_letter_list if i in list(dataframe.letter)]
# print(final)

data_dict ={row.letter:row.code for index,row in dataframe.iterrows() }
#
# final = [data_dict[i]  for i in user_letter_list if i in data_dict.keys()]
# print(final)

final = [data_dict[letter]for letter in user]
print(final)