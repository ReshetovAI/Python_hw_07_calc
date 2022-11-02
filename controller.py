import view
import model


# def initData():
#     a = view.InputData('A')
#     b = view.InputData('B')
#     model.InitA(a)
#     model.InitB(b)


# def PrintValues():
#     a = model.GetA()
#     b = model.GetB()
#     view.OutputData(a)
#     view.OutputData(b)


# def PrintSum():
#     result = model.SumData()
#     view.OutputResult(result)


# def PrintSub():
#     substraction = model.SubData()
#     view.OutputSub(substraction)


# def PrintMult():
#     multiplication = model.MultiData()
#     view.OutputMult(multiplication)


# def PrintDiv():
#     division = model.DivData()
#     view.OutputDiv(division)


def start():
    a = view.InputData('первое')
    model.set_first(a)
    while True:
        oper = view.InputOperator()
        if oper == '=':
            break
        b = view.InputData('второе')
        model.set_second(b)
        model.set_result(oper)
        result = model.get_result()
        if result == None:
            view.division_by_zero()
            break
        first = model.get_first()
        second = model.get_second()
        view.OutputResult(first, second, oper, result)
        view.print_window(result)
        model.set_first(result)
