def openFile():
    try:
        f1 = open('new', 'r')
        while True:
            data = f1.readlines()
            print(data)
            if data[0] != '':
                return data
            elif data[0] != '':
                break
            f1.close()
    except IOError:
        print(IOError.with_traceback())




