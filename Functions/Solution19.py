from functools import reduce
  
fibonacci_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], 
                                 range(n-2), [0, 1]) 
  
print(f'The fibonacci series upto 7 digits using lambda: {fibonacci_series(7)}') 