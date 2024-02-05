def x(y):
    # # z = list(y)
    # sp_ch = ['#','.','/',',',"a"]
    # def remove(chs):
    #       temp = (y)
    #       temp = temp.replace(chs,"")
    #       return temp
    # result = map(remove,sp_ch)

    # return "".join(list(result))
    pass
print(x("mohamed L L , /L ahme,dali ali hassan ali \n"))
def x(y):
    z = list(y)
    sp_ch = ['#','.','/',',',"a"]
    temp = ''
    for x in z:
        if(x not in sp_ch): temp += x
    return temp
    # def remove(chs):
    #       temp = (y)
    #       temp = temp.replace(chs,"")
    #       return temp
    # result = map(remove,sp_ch)

    # return "".join(list(result))
print(x("mohamed L L , / L ahmedali ali hassan ali \n"))