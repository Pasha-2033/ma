def get_file_data(file_name, file_folder, file_type, read_type, read_file):
    error = []
    file_data = None
    try:
        file_name = str(file_name)
        file_folder = str(file_folder)
        file_type = str(file_type)
        read_type = str(read_type)
    except:
        pass
    try:
        file = open(file_folder + file_name + file_type, read_type)
    except:
        error.append(1)
    if read_file != None:
        if type(read_file) == int:
            try:
                file_data = file.readline(read_file)
            except:
                error.append(2)
        elif type(read_file) == list:
            try:
                file_data = []
                for i in range(len(read_file)):
                    file_data.append(file.readline(read_file[i]))
            except:
                error.append(3)
        else:
            error.append(4)
    else:
        try:
            file_data = file.read()
        except:
            error.append(5)
    return file_data
    #if len(error) != 0:
        #return error
    file.close()
a = []            
a.append(str(get_file_data('1', 'C:/Users/user/Desktop/', '.wav', 'rb', None)))
a[0] = a[0].split("x")
#file = open('C:/Users/user/Desktop/' + name + '.wav', 'rb')
open('11.txt', 'w').write(str(a))