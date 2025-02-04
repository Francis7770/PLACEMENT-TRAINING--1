def area_lambda(length, width):
    return reduce(lambda x, y: x * y, [length, width])

# Example usage:
length = 5
width = 8
result = area_lambda(length, width)
print(f&quot;Area of Rectangle: {result}&quot;)
