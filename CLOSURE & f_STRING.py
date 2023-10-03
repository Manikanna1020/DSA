def dummy (person):
    coins=3
   
    def game():
        nonlocal coins
        coins -=1 

        if coins >1 :
            print('\n%s has %s coins left.' %(person,coins))   #%s - IS  ONE OF THE MEHTOD FOR f-STRING
        elif coins==1: 
            print('\n%s has %s coin left.' %(person,coins))
        else:
            print('\n%s is out of coins' %(person))
    return game 

tommy = dummy('Tommy')
rosh = dummy('Rosh')


tommy()
tommy ()

rosh()

#/ IF THE PARANTHESIS IS NOT DECLARE IN CALLING FUNCTION IT WILL RUN UNTILL IT BECOMES NULL VALUE 
# MOST THE "CLOSURE" APPEAR AFTER THE DECLARE OF PARENT CLASS 