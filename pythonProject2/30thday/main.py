"""
try [[error_name]as error_message]:
    -----------------
    -----------------
    ----------------
except[[error_name]as error_message]:
    ------------------
    -----------------
    ------------------
except[[error_name]as error_message]:
    ------------------
    -----------------
    ------------------
else:    ---- if the try block succeed
    ------------------
    ------------------
    -------------------
finally :           --------- no matter what happens
----------------
--------------
-------------
raise can be used the raise the exception to create the error

"""

# file not found error

# key error
# in dictionary if key not exists

# index error
# in list and tuple

# type error
# manipulating between the two different type

# bmi calculator
# !6Z+lB053AL9*66aw7YD6q8d6
# ###########################################
# height = float(input("height"))
# weight = float(input("weight"))
# if height > 3:
#     raise ValueError("human height will not be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)
##################################################
# interactive coding exercise
# fruits = ['APPLE', 'PEAR', 'orange']
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit_pie")
#
#     else:
#         print(fruit + 'pie')
#
#
# make_pie(10)
#######################################################
facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'likes': 13, 'comments': 2, 'shares': 1},
    {'likes': 33, 'comments': 8, 'shares': 6},
    {'comments': 4, 'shares': 2},
    {'comments': 5, 'shares': 5},
    {'likes': 19, 'comments': 3}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        continue
print(total_likes)
#########################################################
# day 29 password manager program extenstion


