with open('Test.txt','r') as f:
    rf=f.read(100)
    print(rf)
    f.seek(0)
    rf=f.read(100)
    print(rf)
