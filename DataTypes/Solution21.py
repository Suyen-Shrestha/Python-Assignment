sample_li = [(2,5),(1,2),(4,4),(2,3),(2,1)]

def sort_tup(tup):
    return tup[1]

print(f'Sample list of tuple before sorting: {sample_li}')
sample_li.sort(key=sort_tup)  
print(f'Sample list of tuple after sorting by last element: {sample_li}')  