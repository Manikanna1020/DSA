def add(num):
    if(num >=9):
        return num+1
    
    total = num+1
    print(total)

    return add(total)

mynew = add(0)
print(mynew)

