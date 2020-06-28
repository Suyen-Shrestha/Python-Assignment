
def sum_of_nums(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum        

numbers = input('Enter list of numbers separated by comma: ').split(',')
nums = [int(x.strip()) for x in numbers]

print(f'The numbers are: {nums}')
total_sum = sum_of_nums(nums)
print(f'The sum of numbers: {total_sum}')
