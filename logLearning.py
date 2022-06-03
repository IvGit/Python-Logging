import logging


logging.basicConfig(filename='mylog.log', level=logging.DEBUG)


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def Multipy(x,y):
    return x*y

def Devide(x,y):
    return x / y

num_1 =10
num_2 = 5

add_re = add(num_1,num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_re))

sub_re = subtract(num_1,num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_re))

multi_re = Multipy(num_1,num_2)
logging.debug('Multi: {} * {} = {}'.format(num_1,num_2,multi_re))

devide_re = Devide(num_1,num_2)
logging.debug('Dvi: {} / {} = {}'.format(num_1,num_2,devide_re))
