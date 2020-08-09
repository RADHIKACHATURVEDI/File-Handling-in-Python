with open('Test1.txt','w') as f:
    f.write('Test')
    f.write('Test')
    
    #return True if the file is writable otherwise False
    print(f.writable())


with open('Test.txt','r') as f:

    #returns False if the mode is r
    print(f.writable())    
    
    