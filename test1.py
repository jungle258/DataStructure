# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
from timeit import Timer


def test1():
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - b - a
            if a**2 + b**2 == c:
                print('a,b,c:%d,%d,%d' % (a, b, c))


def main():
    t = Timer('test1()', 'from __main__ import test1')
    print('time:', t.timeit(number=1), ' second')


if __name__ == '__main__':
    main()
