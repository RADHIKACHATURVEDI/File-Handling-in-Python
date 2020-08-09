with open('Test.txt','r') as f:
    chunk_size=10
    f_contents=f.read(chunk_size)

    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(chunk_size)