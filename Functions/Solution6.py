
def check_range(num,R1,R2):
    if R1 <= num <= R2:
        print(f'The no. is in the range!')
    else:
        print(f'the no. is not in the range!')


start_point = input('Enter the starting value of range: ')
end_point = input('Enter the ending value of range: ')
number = input('Enter a number: ')

check_range(number,start_point,end_point)
