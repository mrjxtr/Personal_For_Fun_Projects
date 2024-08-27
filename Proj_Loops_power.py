def raise_power(number, power):
    result = 1
    for index in range(power):
        result = result * number
    return result


numberX = int(input("Input number: "))
powerX = int(input("Input power: "))
print(raise_power(numberX, powerX))
