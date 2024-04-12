def get_number(index):
    if index%3 == 1:
        num = 4 + 7* (index//3)
    elif index%3 == 2:
        num = 8 + 7* (index//3)
    else:
        num = 7*(index//3)
    print(num)


get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70