def mango(a, b):
    price = a * b - a//3*b
    return f'{price} # {a-a//3} mangoes for ${b} per unit = ${price}; {a//3} for free'
print (mango(2, 3))
print (mango(3, 3))
print (mango(9, 5))
