import controller


# def CalcData():
#     pass


# a = 0
# b = 0
# listOmerator = ['*', '/', '+', '-']


# def InitA(number: int):
#     global a
#     a = number


# def InitB(number: int):
#     global b
#     b = number


# def GetA():
#     global a
#     return a


# def GetB():
#     global b
#     return b


# def SumData():
#     global a
#     global b
#     return a+b


# def SubData():
#     global a
#     global b
#     return a-b


# def MultiData():
#     global a
#     global b
#     return a*b


# def DivData():
#     global a
#     global b
#     return int(a/b)


first = 0
second = 0
result = 0

listOperator = {'*': lambda x, y: int(x) * int(y),
                '/': lambda x, y: int(x) / int(y),
                '+': lambda x, y: int(x) + int(y),
                '-': lambda x, y: int(x) - int(y)}


def set_first(number: int):
    global first
    first = number


def set_second(number: int):
    global second
    second = number


def set_result(oper: str):

    # ДЕЛЕНИЕ НА НОЛЬ!!!!
    global result
    global second
    result = listOperator.get(oper)(first, second)


def get_first():
    global first
    return first


def get_second():
    global second
    return second


def get_result():
    global result
    return result
