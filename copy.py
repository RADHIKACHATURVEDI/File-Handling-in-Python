with open('Test.txt','r') as rf:
    with open('Test_Copy','w') as wf:
        for line in rf:
            wf.write(line)
            