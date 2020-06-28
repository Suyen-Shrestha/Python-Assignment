integer_li = [1,2,3,4,5,6,7,8]

def squareCube(int_list):
    square_li = list(map(lambda n: n**2,integer_li))
    cube_li = list(map(lambda n: n**3,integer_li))
    return square_li, cube_li

print(f'The sample list: {integer_li}')
print(f'List of squares and cubes of each integer in sample list: {squareCube(integer_li)}')   