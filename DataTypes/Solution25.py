sample_list1 = [{},{},{}]
sample_list2 = [{1,2},{},{}]



def check_for_empty_dict(li_dict):
    """
        function for checking list containing empty dictionary.
    """
    value = True
    for item in li_dict:
        if len(item) != 0:
            value = False
    return value

value1 = check_for_empty_dict(sample_list1)
value2 = check_for_empty_dict(sample_list2)


print(f'First Sample list: {sample_list1}')             
print(f'First Return Value: {value1}')

print(f'First Sample list: {sample_list2}')             
print(f'First Return Value: {value2}')