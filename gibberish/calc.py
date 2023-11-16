
def add(x, y):
  result = x + y
  return result

def subtract(x, y):
  result = x - y
  return result

def multi(x, y):
  result = x * y
  return result

def div(x, y):
  if y == 0:
    raise ValueError('cannot divide by zero')
  return x / y