import gevent
from gevent import monkey
import time

monkey.patch_all()
b = []
a = [5, 4, 6]


def f1(n, j):
    print(f'等候{j}')
    for i in range(n):
        time.sleep(0.5)
        print(gevent.getcurrent(), i)


def main():
    for i in a:
        b.append(gevent.spawn(f1, i, i/2))
    gevent.joinall(
        b
    )


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    print(f'此次运行花费时间{time.perf_counter()-t1}秒')