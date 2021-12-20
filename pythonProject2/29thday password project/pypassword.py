import random


def list_formation(n, lis):
    s = [random.choice(lis) for _ in range(n)]
    return s


def passwordfunc():
    # #############################################
    # #password generator
    # ###############################project day 5
    # #concept of loop
    # #for item in list:
    #   #do something to each item
    # #######################################################################
    # # fruits=['Apple','peach','pear']
    # # for i  in fruits:
    # #   print(i)
    # #   print(i+"pie")
    # # print(fruits)
    # ############################################################################
    # #interactive coding exercise
    # # student_heights=input("input the student heights").split()
    # # s=0
    # # num=0
    # # print(student_heights)
    # # for n in student_heights:
    # #   s+=int(n)
    # #   num+=1
    # # print("average of the student height" ,round(s/num))#############################################################################
    # #interactive coding exercise
    # ##############  highest score
    #
    # # student_score=input("input a list of student 's scores").split()
    # # key =student_score[0]
    # # for score in student_score:
    # #   if key<score:
    # #     key,score=score,key
    # # print(key)
    # ##############################################################################
    # #for loop in range operator
    # ###########################################################################
    # #for number in range(a,b):
    #   #print(number)
    # ##############################################################
    # # total=0
    # # for number in range(1,101):
    # #   total+=number
    # # print(total)
    # ###############################################################################
    # #interactive coding exercise
    # ##########################################################################
    # # total=0
    # # for number in range(2,101,2):
    # #   total+=number
    # # print(total)
    # ############################################################################
    # # total=0
    # # n=float(input("input the number of terms"))
    # # x=(n/2)*((n/2)+1)
    # # print(x)
    # # ######################################################################
    # # total=0
    # # for number in range(1,101):
    # #   if number%2==0:
    # #     total+=number
    # # print(total)
    # ######################################################################
    # #interactive coding exercise
    # #####################################################################
    # #fizz buzz
    # for i in range(1,101):
    #   if i%3==0 and i%5==0:
    #     print("fizz buzz")
    #   elif i%3==0:
    #     print("fizz")
    #   elif i%5==0:
    #     print("buzz")
    #   else:
    #     print(i)
    ########################################################################
    # pypassoword generator project
    ########################################################################

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 20)
    nr_symbols = random.randint(2, 12)
    nr_numbers = random.randint(2, 12)
    lisr_con = list_formation(nr_letters, letters) + list_formation(nr_symbols, symbols) + list_formation(nr_numbers,numbers)
    # easy level
    string = "".join(lisr_con)
    print('easy_level')
    print(string)
    print('higher_level')
    # hard level
    random.shuffle(lisr_con)
    pypassword = "".join(lisr_con)
    return pypassword

#########alternate for shuffle
# rand=[1,2,3,4,5,6,7,8,9,10]
# random.shuffle(rand)
# mylist=[ lisr_con[i]   for i in rand]
# for i in mylist :
#   print(i,end="")


# hardlevel

###########################################################################################
