import random
def HumansTurn(candyAmount):
    takenCandies = int(input("Сколько конфет возьмёте? (не более 28): "))
    if takenCandies < 29:
        candyAmount -= takenCandies
    else: print("Можно взять не более 28!")
    return candyAmount
def MachinesTurn(candyAmount):
    if candyAmount > 28:
        takenCandies = random.randint(1,28)
    else: takenCandies = random.randint(1,candyAmount)
    print("Компьютер взял {} конфет.".format(takenCandies))
    candyAmount -= takenCandies
    return candyAmount
candyAmount = 120
while candyAmount > 0:
    print("На столе {} конфет.".format(candyAmount))
    candyAmount = HumansTurn(candyAmount)
    print("На столе {} конфет.".format(candyAmount))
    if candyAmount > 0:
        candyAmount = MachinesTurn(candyAmount)
    else: print("Вы выиграли!")