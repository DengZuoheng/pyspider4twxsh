def read_urls(filename):
    lst=[]
    f=open(filename)
    while True:
        line=f.readline()
        if not line:
            break
        lst.append(line)
    f.close()
    return lst