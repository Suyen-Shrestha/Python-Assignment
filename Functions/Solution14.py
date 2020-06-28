
sample_dict_li = [{'name': 'Ramesh', 'city':'kathmandu'}, {'name': 'Geeta', 'city': 'Bhaktapur'}, {'name': 'Hari', 'city': 'Chitwan'}]

def sort_dict_by_lambda(input_dict_li):
    sorted_dict_li = sorted(input_dict_li,key=lambda a: a['city'])
    return sorted_dict_li

print(f'The list of sample dictionary before sorting: {sample_dict_li}')
print(f'The list of sorted dictionary using lambda function: {sort_dict_by_lambda(sample_dict_li)}')