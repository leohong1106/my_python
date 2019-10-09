#구구단 2단
for i in range(1,10):
    print('{}x{}={}'.format(2,i,2*i))

#구구단 2~9단
for x in range(2,10):
    for y in range(1,10):
        print('{}x{}={}'.format(x,y,x*y))