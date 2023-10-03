user = ['kanna','Madu','PR']

data =['kanna',21,True]

emptylist = []

print('Kanna' in emptylist)

print(user[0])
print(user[-2]) 

print(user.index('PR'))
print(user[0:2])

print(len(data))            #len(data) - TELLS THE HOW MANY STRINGS IN THE INPUT
user.append('kiruthik')     #append('') - IT WILL ADDS THE EXTRA ELEMENT TO THE INPUT 
print(user)

user +=['srihari']                 
print(user)

user.extend(['Roshni','vidhiya'])  # IT ALSO ADD ELEMENT TO USER INPUT BUT IT WILL ENCLOSED WITH THE SQUARE BRACKET
print (user)

user.remove('vidhiya')       #remove - IT WILL REMOVE THE ELEMENT FROM THE INPUT
print(user)

user.sort()                    #sort - IT WILL SORT THE ENTIRE INPUT 
print(user)


nums=[2,44,33,88,77]
nums.sort(reverse=False)       # reverse=True - THIS WILL PRINT NUMBERS IN DESCENDING ORDER 
print(nums)                    # reverse = False - THIS WILL PRINT NUMBER IN ASCENDING ORDER

numsvalue= nums.copy()
mynums = list(nums)

print(numsvalue)
mynums.sort(reverse=True)
print(mynums)
