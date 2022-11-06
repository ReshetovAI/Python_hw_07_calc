import model
import view


model.string = input('Введите выражение: ')


def division_be_zero():
    print("Деление на ноль!")
    exit()


def printResult():
    print(f'{model.string} = {model.result}')
