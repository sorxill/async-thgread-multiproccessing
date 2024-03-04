import threading
import time


def get_data(data):
    while True:
        print(f"{threading.current_thread().name}: {data}")
        time.sleep(1)


def thread_start():
    d = threading.Thread(target=get_data, args=(time.time(),), name="thread-1")
    d.start()


def range_to_10():
    for i in range(10):
        print(f"score: {i}")
        time.sleep(1)
        if i == 5:
            threading.main_thread().name = "result"


"""
Если запустить thread_start и range_to_10 одновременно
range_to_10 будет работать в Main потоке, а thread_start в своем потоке, и не всегда порядок вывода будет очевиден
"""


def range_to_100():
    """Смотрим текущий поток - он будет main, все потоки и активное количество"""
    for i in range(100):
        print(f"score: {i}")
        time.sleep(1)

        if i % 10 == 0:
            print("name:", threading.current_thread().name)
            print("enum:", threading.enumerate())
            print("active:", threading.active_count())

################################################################


def get_data_value(data, value):
    for _ in range(value):
        print(f"{threading.current_thread().name}: {data}")
        time.sleep(1)


thread_list = []


def thread_lists():
    for i in range(5):
        thr = threading.Thread(target=get_data_value, args=(time.time(), i, ), name=f"[thread-{i}]: ")
        thread_list.append(thr)
        thr.start()


def start_threads_from_list():
    """Join блокирует выполнение кода на данном месте, пока не выполнятся все ранее запущенные потоки"""
    for i in thread_list:
        i.join()


if __name__ == "__main__":
    thread_lists()
    start_threads_from_list()
    print("finish")
