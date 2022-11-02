import controller


def CalcData():
    pass


a = 0
b = 0
listOmerator = ['*', '/', '+', '-']


def InitA(number: int):
    global a
    a = number


def InitB(number: int):
    global b
    b = number


def GetA():
    global a
    return a


def GetB():
    global b
    return b


def SumData():
    global a
    global b
    return a+b


def SubData():
    global a
    global b
    return a-b


def MultiData():
    global a
    global b
    return a*b


def DivData():
    global a
    global b
    return int(a/b)
