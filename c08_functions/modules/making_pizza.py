# variant 1
#import pizza

#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# variant 2
#from pizza import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# variant 3 using n alias for a function
from pizza import make_pizza as my_make
my_make(16, 'pepperoni')
my_make(12, 'mushrooms', 'green peppers', 'extra cheese')

# variant 4 import all methods
#from pizza import *
