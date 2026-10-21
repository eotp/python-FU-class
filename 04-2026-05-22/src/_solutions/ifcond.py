for i in range(10):
    print(i)
    
    if i > 3:
        break
        
    if i > 2:
        print('three')
    elif i > 1:
        print('two')
    elif i > 0:
        print('one')
    else:
        print('zero')