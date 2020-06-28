sample_li = input('Enter a sample list separated by comma: ').split(',')
edited_li = [x.strip() for x in sample_li]

final_tup = tuple(edited_li)

print(f'The initial list before conversion: {edited_li}')
print(f'The final tuple after conversion: {final_tup}')