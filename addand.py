#This program will put values entered by user in a list then
#values will be printed out and display
#them in a comma form with 'and' at the end of the last vlaue


def combo(list):
    listvalue = 0 
    last =(len(list))
    print(len(list))
    while True:
        if (listvalue +1 )  == last:
            print('and ' + list[listvalue] , end = ' '  )
            break
        else:
            print(list[listvalue] + ',' , end = ' ' )
            listvalue += 1  
            
            
values = []
print('Enter Items enter nothing to end Items')
while True:
    items = input()
    if items == '':
        break
    values.append(items)
combo(values)

