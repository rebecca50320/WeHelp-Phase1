def find(spaces, stat, n):
    #相乘找available
    available = []
    for i in range(len(spaces)):
        available.append(spaces[i]*stat[i])
        
    #best fit
    if n > max(available):
        print(-1)
    else:
        while n <= max(available):
            if n in available:
                print(available.index(n))
                break
            else:
                n+=1
            

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2