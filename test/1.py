import sympy

x = sympy.Symbol('x')
n = 0

# print(sympy.solve(((((((x-1)/5*4-1)*5/4-1)*5/4-1)*5/4-1)*5/4-4),x))
while True:
    a = sympy.solve(((((((x - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4 - n), x)
    # a = sympy.solve((x-1)/5*4-4)
    if a[0].is_integer:
        break
    n += 1
    print(a)
    print('n = %s' % n)
print(a)

# a = (((((3121 - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4 - 1) / 5 * 4
# print(a)
#
# b = (((((3121 - 1) / 5 * 4 - 1) / 5 * 4) - 1) / 5 * 4 -1) / 5 * 4 - 1
# print(b)

# a = sympy.solve((x-1)/5*4-8)
# print(a)
# b = a[0]
# print(b)
# # b = sympy.Symbol('b')
# print(a.is_integer)
# print(type(b)) #<class 'sympy.core.numbers.Integer'>
# # <class 'sympy.core.numbers.Rational'>
