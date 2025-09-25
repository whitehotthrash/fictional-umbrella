def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


assert isEven(2) == True
assert isEven(3) == False
