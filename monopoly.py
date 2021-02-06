import random

def monopoly():
    spacesLanded = [0 for _ in range(40)]
    random.seed()
    currentSpace = 0
    for i in range(100000):
        diceA = random.randint(1,6) 
        diceB = random.randint(1,6)
        currentSpace += diceA + diceB
        if currentSpace >= 40:
            currentSpace = currentSpace%40
        spacesLanded[currentSpace] += 1
    print(spacesLanded[0:9])
    print(spacesLanded[10:19])
    print(spacesLanded[20:29])
    print(spacesLanded[30:39])

if __name__ == '__main__':
    monopoly()
