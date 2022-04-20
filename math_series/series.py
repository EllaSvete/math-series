def fibonacci(n):
  """
 this function will return the nth value of the fibonacci series
  """
  if n <= 1:
    if n==0:
      return 0
    else:
      return 1
  return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  """
 this function will return the nth value of the lucas series
  """
  if n <= 1:
    if n==0:
      return 2
    else:
      return 1
  return lucas(n-1) + lucas(n-2)
  

def sum_series(n, x = 0, y = 1):
  """
 this function will determine whether or not the values of your input are part of the fibonacci series or the lucas series
  """
  if n == 0:
    return x
  elif n == 1:
    return y
  return sum_series(n-1,x,y) + sum_series(n-2,x,y)

  