import view
import model


def initData():
    a = view.InputData('A')
    b = view.InputData('B')
    model.InitA(a)
    model.InitB(b)


def PrintValues():
    a = model.GetA()
    b = model.GetB()
    view.OutputData(a)
    view.OutputData(b)


def PrintSum():
    result = model.SumData()
    view.OutputResult(result)


def PrintSub():
    substraction = model.SubData()
    view.OutputSub(substraction)
