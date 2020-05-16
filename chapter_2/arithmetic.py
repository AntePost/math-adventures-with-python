def average(a, b):
    return (a + b) / 2


def my_sum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum

def my_sum2(num):
    running_sum = 0
    for i in range(0, num+1):
        running_sum += i**2 + 1
    return running_sum

def average3(num_list):
    return sum(num_list) / len(num_list)

print(average3([53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]))