
def unique_list(input_li):
    unique_li = []
    for item in input_li:
        if item not in unique_li:
            unique_li.append(item)
    return unique_li


items_li = input('Enter a list of items separated by comma: ').split(',')
edited_li = [x.strip() for x in items_li]
final_li = unique_list(edited_li)
print(f'The unique list of items: {final_li}')