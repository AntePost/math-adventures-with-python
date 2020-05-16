def factors(num):
    '''returns a list of the factors of num'''
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list

def dfc(a, b):
    a_factors = factors(a)
    b_factors = factors(b)
    return [value for value in a_factors if value in b_factors][-1]

print(dfc(150, 138))