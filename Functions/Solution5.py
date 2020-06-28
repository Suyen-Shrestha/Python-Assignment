
def factorial(num):
    if num > 0:
        if num == 1 or num == 0:
            return num    
        else:
            return num * factorial(num-1)    
    else:
        print('Please enter a non-negative number!')

num = int(input('Enter a number to calculate factorial: '))
fact = factorial(num)
print(f'Factorial: {fact}')