def even():
    a = int(input("Enter a minimum value: "))
    b = int(input("Enter a maximum value: "))
    
    while (a < b):
        if (a % 2 == 0):
            print (a)
            a = a + 2
        else:
            a = a + 1
        
    
even ()