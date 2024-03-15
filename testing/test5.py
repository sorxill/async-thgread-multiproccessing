"""
Semaphore и Barrier - Семафоры разрешают выполнение только заданного числа потоков,
следующие потоки начинают выполняться по мере окончания предыдущих
Barrier - пока все потоки, вызванные в определенном количестве потоков(например 5) не вызовут метод wait - исполнение
других потоков не будет запущенно. Некая противоположность семафоре, сделана(наверно) для целостности потоков
"""

import random
import threading
import time
from threading import Thread, BoundedSemaphore, Barrier

# max_connections = 5
# pool = BoundedSemaphore(value=max_connections)
# """Создаем максимальное количество исполняемых потоков + создаем семафору, которая будет ограничивать потоки"""
#
#
# def test():
#     """С помощью семафоры смотрим количество исполняемых потоков
#     Внутри задаем рандомное 'время' работы потока с помощью sleep"""
#     with pool:
#         sleep_time = random.randint(3, 5)
#         print(f"current - {threading.current_thread().name}, спит - {sleep_time} seconds")
#         time.sleep(sleep_time)
#
#
# for i in range(10):
#     """Создаем 10 потоков и присваиваем их функции test, запускаем потоки"""
#     thr = Thread(target=test, name=f"{i}").start()

########################################################################


def test_2(barrier):
    """
    В данной функции мы передаем в параметры барьер, с количеством ожидающих потоков
    После того как все потоки дойдут до строчки barier.wait() все потоки в заданном количестве пройдут его одновременно
    :param barrier:
    :return:
    """
    slp = random.randint(5, 10)
    time.sleep(slp)
    print(f"{threading.current_thread().name} запущен в ({time.ctime()}), спит - {slp} seconds")

    barrier.wait()

    print(f"{threading.current_thread().name} завершил работу в  ({time.ctime()})")


max_barr = 5
barr = Barrier(parties=max_barr)

for i in range(10):
    """
    Создаем 10 потоков и передаем в качестве аргумента барьер
    """
    thr = Thread(target=test_2, args=(barr,), name=f"{i}").start()
