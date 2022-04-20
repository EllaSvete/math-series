from math_series.series import lucas, sum_series, fibonacci

# fibonacci 0, 1, 1, 2, 3, 5, 8, 13, ...
# lucas 2, 1, 3, 4, 7, 11, 18, 29, ...

def test_fibonacci_for_type():
  assert type(fibonacci(3)) is int

def test_fibonacci_one():
  expected = 1
  actual = fibonacci(2)
  assert actual == expected

def test_fibonacci_two():
  expected = 13
  actual = fibonacci(7)
  assert actual == expected

def test_lucas_one():
  expected = 3
  actual = lucas(2)
  assert actual == expected

def test_lucas_two():
  expected = 29
  actual = lucas(7)
  assert actual == expected

def test_sum_series_one():
  expected = 8
  actual = sum_series(6, 0, 1)
  assert actual == expected

def sum_series_series_two():
  expected = 7
  actual = sum_series(29, 2, 1)
  assert actual == expected