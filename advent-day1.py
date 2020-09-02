f = open('advent-day1-source.txt')


def calculateFuelFor(fuel):
    return (int(fuel / 3) - 2)


def getTotalFuel(num, total):
    fuel = calculateFuelFor(num)
    if (fuel <= 0): return total
    return getTotalFuel(fuel, total + fuel)

result2 = sum((getTotalFuel(int(moduleWeight), 0) for moduleWeight in f))

print(result2)
