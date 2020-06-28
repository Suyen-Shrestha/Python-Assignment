def get_even_li(input_list):
    even_li = [x for x in input_list if (x%2) == 0]
    return even_li

sample_li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = get_even_li(sample_li)

print(f'Sample list: {sample_li}')
print(f'Even list: {even_list}')