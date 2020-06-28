
def mul_of_nums(num_list):
    mul = 1
    for num in num_list:
        mul *= num
    return mul        

numbers = input('Enter list of numbers separated by comma: ').split(',')
nums = [int(x.strip()) for x in numbers]

print(f'The numbers are: {nums}')
total_mul = mul_of_nums(nums)
print(f'The multiplication of numbers: {total_mul}')
