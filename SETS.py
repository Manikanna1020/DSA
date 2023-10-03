num ={1,3,4,6}

num1= set((1,2,4,6))

print(num)
print(num1)

# SET DOESNOT PRINT DUPLICATE VALUES IN TH OUTPUT 
num ={1,3,3,4,5}
print(num)

# # TRUE IA DUPE OF 1, FALSE IS DUPE OF 0
# num ={True,2,True,3,False,4}
# print(num)

# IF YOU WANT TO UPDATE ONE TO ANOTHER
num2={6,9,100}
num.update(num2 | num1)
print(num)
