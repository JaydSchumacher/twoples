def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply(2,5,10,90,85,5,8,7))