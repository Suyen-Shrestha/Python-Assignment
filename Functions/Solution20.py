def array_intersect(array1,array2):
 return list(filter(lambda x: x in array1, array2)) 

arr1= [1,5,9,8,5,6]
arr2=[4,5,8,3]

print(f'Two sample arrays are: {arr1}, {arr2}')
print(f'Intersection of two arrays: {array_intersect(arr1,arr2)}')