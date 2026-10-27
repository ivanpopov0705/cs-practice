def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


print("Калькулятор запущен")
print("2 + 2 =", add(2, 2))
print("5 - 3 =", subtract(5, 3))
print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))

