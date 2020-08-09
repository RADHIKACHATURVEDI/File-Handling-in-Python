with open('Test.txt') as f:
    f_contents=f.readline()
    print(f_contents)
    print(f.tell())
    f_contents=f.readline()
    print(f.tell())
    print(f_contents)    
    print(f.tell())