def stringCSVToList(str):
    list = []
    while len(str) > 0:
        word = ""
        while str[0] != ',':
            if len(str) == 1:
                word = word + str
                list.append(word)
                str = ""    
                break
            word = word + str[0]
            str = str[1::]
        else:
            list.append(word)
            str = str[2::]
    else:
        print(list)
