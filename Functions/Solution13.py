
sample_tuple_li = [('red',5),('orange',9),('green',3),('blue',7)]

print(f'Sample tuple before sorting: {sample_tuple}')

def sort_tuple_by_lambda(input_tuple_li):
    """
        function for sorting list of tuple by second items in each tuple.
    """
    return input_tuple_li.sort(key=lambda a: a[1])


sort_tuple_by_lambda(sample_tuple_li)
print(f'Tuple after sorting using lambda funtion: {sample_tuple_li}')