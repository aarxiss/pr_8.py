composite_numbers = [x for x in range(2, 101) if len([i for i in range(1, x + 1) if x % i == 0]) > 2]
print(composite_numbers)
