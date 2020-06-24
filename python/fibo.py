import sys
if __name__ == '__main__':

    def F():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib = F()
    for i in range(0, 15):
        print(next(fib))
    sys.exit(0)
