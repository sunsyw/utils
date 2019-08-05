# a = [x for x in range(10)]
# print(a)
#
# b = (x for x in range(10))
# print(b)
# for b1 in b:
#     print(b1)


def generator():
    a, b = 0, 1
    for i in range(10):
        yield b
        a, b = b, a+b


if __name__ == '__main__':
    print(generator())
    a = generator()
    print(next(a))
    # for i in a:
    #     print(i)