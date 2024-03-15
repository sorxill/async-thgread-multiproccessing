"""
Здесь будет про Condition и Event - такие небольшие endpoints, которые могут передавать состояние
Event имеет только два состояния - True/False - когда True поток выполняется.
Event имеет два метода set/clear - Изначально состояние False поток будет приостановлен на точке event.wait()
"""
import random
import threading
import time
#
# event = threading.Event()
#
#
# def print_test():
#     while True:
#         event.wait()
#         print("Test printed")
#         time.sleep(5)
#
#
# thr = threading.Thread(target=print_test)
# thr.start()

################################################################
#
# event = threading.Event()
#
#
# def image_handler():
#     slp = random.randint(5, 10)
#     now_time = time.ctime()
#     print(f"Изображение из потока {threading.current_thread().name} - в обработке {slp} seconds, {now_time}")
#     time.sleep(slp)
#     event.wait()
#     print(f"Изображение из потока {threading.current_thread().name} отправлено в БД, {time.ctime()}")
#
#
# for i in range(1, 11):
#     thr = threading.Thread(target=image_handler, name=f"[thr-{i}]")
#     thr.start()
#
#
# if threading.active_count() >= 11:
#     print("Количество потоков больше 11")
#     event.set()
#
################################################################

cond = threading.Condition()


def test_func_1():
    """
    Функция, которая постоянно проверяет состояние cond в том случае, если пришло уведомление выполняет вывод на экран
    о том, что значение делится на 10
    :return:
    """
    while True:
        with cond:
            cond.wait()
            print("Число делимое на 10")


def test_func_2():
    """
    Функция, которая прогоняет значения от 1 до 100, в том случе если делиться на цело на 10 изменяет
    состояние на активное, иначе просто выводи в консоль текущее значение
    :return:
    """
    for i in range(1, 100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"число: {i}")
        time.sleep(0.05)


thr1, thr2 = threading.Thread(target=test_func_1), threading.Thread(target=test_func_2)
thr1.start()
thr2.start()

"""
Для того, чтобы корректно успевал работать первый поток, а именно открывать состояние для condition
необходимо брать задержку 
"""
