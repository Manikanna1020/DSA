def hello():
    print('Hello World')

hello()               # IF WE DOES NOT DEFINE THE CLASS IT WILL COMPILE THE LAST PROGRAM

def sum(num1,num2):
    return num1 + num2

total = sum(8,92)
print (total)

def items(*jk):            #jk consider as dummy name you can use any words
    print(jk)
    print(type(jk))

items('kanna',24,'Marry')

def items1(**jk):
    print(jk)                   # WHEN WE USE ** IT REPRESENT THE KEYWORD FUNCTIONS WHICH IS "dictonary"
    print(type(jk))
items1(name='Kanna', last='Mani')