def average(a, b):
    return (a + b) / 2

def square_root(num, low, high):
    '''Finds the square root of num by
    playing the Number Guessing Game
    strategy by guessing over the
    range from "low" to "high'''
    for i in range(20):
        guess = average(low, high)
        if guess**2 == num:
            break
        elif guess**2 > num: #"Guess lower."
            high = guess
        else: #"Guess higher."
            low = guess
    return guess

result = square_root(50000, 100, 300)
print(result)
print(result**2)