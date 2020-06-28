def unknown_mul(num):
    return lambda x: x * num

intial_result = unknown_mul(5) # here, 5 is assumed as unknown no.
print(intial_result(8))    # here, 8 is the no. to be multiplied with unknown no.