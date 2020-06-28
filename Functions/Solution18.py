
check_num = lambda n: n.replace('.', '').isdigit() # replacing the decimal '.' with '' and checking for numeric

check_negative = lambda x: check_num(x[1:]) if x[0] == '-' else check_num(x) # checking numeric for both negative and non-negative numbers case.

str1 = '-1234'
str2 = 'asdf234'
str3 = '45.66'
str4= '-45.66'
print(f'The sample strings are:\n{str1}\n{str2}\n{str3}\n{str4}')

print(f'The results for respective strings (True: is a number and False: is not a number):')
print(check_negative(str1))
print(check_negative(str2))
print(check_negative(str3))
print(check_negative(str4))