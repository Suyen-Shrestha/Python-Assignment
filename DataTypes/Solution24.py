import copy

sample_li = input('Enter a list of items separated by space:'). split(' ')

copied_li = []

copied_li = copy.deepcopy(sample_li)

print(f'The original list: {sample_li}')
print(f'The copied list: {copied_li}')
