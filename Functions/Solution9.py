
def check_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True     

number = int(input('Enter a number: '))
result = f'The no. {number} is prime.' if check_prime(number) else f'The no. {number} is not prime.'
print(result)              