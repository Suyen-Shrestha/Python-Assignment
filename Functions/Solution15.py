integer_li = [11,22,33,44,55,66,77,88,99]

def filter_by_lambda(int_list):
    """
        Function implementing lambda to filter even numbers from list.
    """
    return list(filter(lambda n: n%2 == 0, int_list))


evens_li = filter_by_lambda(integer_li)

print(f'The sample integer list: {integer_li}')
print(f'The filtered list of even integers: {evens_li}')
