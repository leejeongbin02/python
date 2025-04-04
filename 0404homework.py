i, n = 0, 0
for i in range(2, 10, 1):
    print("#  %d단  #" %(i), end = " ")
print( )
for n in range(1, 10, 1):
    for i in range(2, 10, 1):
        print("%dX  %d=  %d" % (i, n, i * n), end = " ")
    print( )
