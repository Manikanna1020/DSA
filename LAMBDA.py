
def square(num) : return num * num 
#lambda num : num * num 

print(square(2))

def addTwo(num): return num+2
#lambda num : num + 2      IT WAS THE ANOTHER FORM OF DECLARATION
print(addTwo(13))

sum = lambda a, b : a + b
print(sum(3,6))

########################################################################

def funcBuilder(x):
    return lambda num : num + x 

add1 = funcBuilder(10)
add2 = funcBuilder(20)

print(add1(7))
print(add2(7))

##########################################################################

numbers = [3,5,7,9,10,2]

square_nums = map(lambda num : num * num, numbers)
print(list(square_nums))

##########################################################################

odd = filter(lambda num : num % 2 !=0, numbers )

print(list(odd))

##########################################################################
from functools import reduce 
 
nums = [1,2,5,8,9]
total = reduce(lambda acc,curr : acc + curr, nums)

print(total)


################### STRINGS ########################
names = ['Kanna', 'PR' , 'MAdu goes to college']

char = reduce(lambda acc, curr : acc + len(curr), names , 0)

print(char)