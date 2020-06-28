
sample_str = input('Enter a sample sentence where \'not\' follows the \'poor\': ')

not_indexes = [ i for i in range(len(sample_str)) if sample_str.find('not', i) == i] # list of all occurences of 'not' in sample string

final_str = sample_str # putting a copy of sample_str in the final string

if not_indexes:
    for indx in not_indexes:
        index_of_poor = sample_str.find('poor', indx + 1)
        if index_of_poor != -1 and index_of_poor > indx:
            final_str = final_str.replace(sample_str[indx:index_of_poor+4],'good')                 
        else:
            print('There is no \'poor\' followed by the \'not\' in the provided sentence!')  

else:
    print('There is no \'not\' in the provided sentence!')

print(f'Sample string: {sample_str}')
print(f'Final Result: {final_str}')