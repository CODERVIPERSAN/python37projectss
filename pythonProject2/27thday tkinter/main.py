# gui tkinter
# create labels
# to create button  and its responses
# text input and layout and design the program

# default arguments *arg **kargs in python
############################################################
# convertor
# tkinter
# advanced python arguments
def pypy(a=1, *k):  # --default argument is a *k is the many positional arguments
    return k


def add(*args):  # --unlimited positional arguments
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 48, 35, 65, 2))


# def gcd(*args):
#
#     for j in args:
#         k = [i for i in args if j%i==0]
#         if len(k)==1:
#             print(k[0])
#
# print(gcd(30,50,10,64,8,30,15,6))

def calc(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiple']
    print(n)


calc(2, add=3, multiple=5)

class Car:
    def __init__(self,**kwargs):
        self.modal = kwargs.get('model')
        self.number= kwargs.get('number')
        self.seats = kwargs.get('seats')

car =Car(modal="hyndai")
# print(car.number)