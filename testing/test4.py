"""
Про Timer и его особенности:
Timer не блокирует другие потоки, он ставит в ожидание поток, которому передан target.
Timer наследуется от Thread - у него есть все методы как и обычного потока (можно установить демон
и поток закончится вместе с основным), а так же есть дополнительный метод cancel который отменяет его(про него нужно
ещё почитать).
Так же тут немного про local значения - значения внутри потока. Доступа извне у нас нет.
"""

import threading
import time


def test_print():

    while True:
        print("test")
        time.sleep(1)


timer = threading.Timer(3, test_print)
timer.daemon = True
"""Устанавливаем аргумент демона на True - тк родительский класс - Thread"""
timer.start()

for _ in range(5):
    print("1")
    time.sleep(1)

################################################################

data = threading.local()


def get_name():
    print(f"{threading.current_thread().name}: {data.name}")


def thread1():
    data.name = "Thread1"
    # time.sleep(10)
    get_name()


def thread2():
    data.name = "Thread2"
    get_name()


threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()

# time.sleep(2)
# print(data.name)
"""Тут мы получим ошибку, если попытаемся узнать имя у текущего потока(который спит) из вне - из main потока"""
