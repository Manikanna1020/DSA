name = 'kanna'    # GLOBAL FUNCTION - THIS WILL RUNS ONLY IN 1st DEFINTION ONLY 
count = 1
    
def dummy1():
    color = 'blue'
    global count 
    count +=1
    print(count)
    print(name)

    def dummy(name):
        nonlocal color
        color = 'red'   #nonlocal -IT WILL ASSIGN THE VALUE WHICH WAS BY ME AT WHERE THE KEYWORD IS USED
        print(name)
        print(color)
    dummy('Mani')
     
dummy1()

# GLOBAL VARIBALE IS NOT USE UNLESS IT APPLICABLE

