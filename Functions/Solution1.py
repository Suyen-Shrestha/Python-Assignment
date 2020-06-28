
def max_num(num_list):
    largest_num = num_list[0]
    for num in num_list[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num        

numbers = input('Enter three numbers separated by comma: ').split(',')
nums = [int(x.strip()) for x in numbers]

print(f'The numbers are: {nums}')
largest = max_num(nums)
print(f'The largest number is: {largest}')
