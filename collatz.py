#Collatz Sequence
#Objectives

print('Please Enter a Number')
number = input()



def collatz(Number):
    if Number == 1:
        return
    elif Number % 2 == 0:
        Number = Number // 2
        print (Number)
        return collatz(int(Number))
    elif Number % 2 == 1:
        Number = 3 * Number + 1
        print (Number)
        return collatz(int(Number))
    elif Number == 1:
        return
    else:
        sys.exit()
            

    

collatz(int(number))

