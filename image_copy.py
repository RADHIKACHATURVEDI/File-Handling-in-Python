with open('Walker-memorial-spring-MIT.jpg','rb') as rf:
    with open('MIT_Copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)