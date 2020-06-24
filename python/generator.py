import sys


def gen():
    for i in range(0, 100000):
        yield i ** 2


if __name__ == '__main__':
    my_list = [i for i in range(0, 10000)]
    no_gen = [x**2 for x in my_list]
    generator1 = (x ** 2 for x in my_list)
    generator2 = gen()

    for i in no_gen:
        print(i)

    for i in generator1:
        print(i)

    for i in generator2:
        print(i)

    print('No gen size: ' + str(sys.getsizeof(no_gen)))
    print('generator1 size: ' + str(sys.getsizeof(generator1)))
    print('generator2 size: ' + str(sys.getsizeof(generator2)))
