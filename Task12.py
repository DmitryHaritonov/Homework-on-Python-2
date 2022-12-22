import random

def TwelveTask():
    num1 = round(random.randint(1, 1000))
    num2 = round(random.randint(1, 1000))
    s = num1 + num2
    p = num1 * num2
    print(f"Петя загадал два числа вот их сумма {s} и произведение {p}")
    print("Катя перебором решила найти эти числа")
    x = 1
    hundred = 0
    fifty = 0
    ten = 0
    for _ in range(0, s//2+1):
        y = s-x
        print(f"{x} x и {y} y")
        if p == x*y:
            print(f'Два числа которые загадал Петя {x} и {y} ')
            break
        if x * y < p and hundred != 1:
            x = x + 100
            if x * y > p:
                x = x - 100
                hundred = 1
        elif x * y < p and fifty != 1:
            x = x + 50
            if x * y > p:
                x = x - 50
                fifty = 1
        elif x * y < p and ten != 1:
            x = x + 10
            if x * y > p:
                x = x - 10
                ten = 1
        x += 1

TwelveTask()
