"""
Здесь начинаем проходить multiprocessing
Процесс имеет собственный pid в системе. Может получить его статус(is_alive()), получить его pid (prc.pid),
уничтожить процесс с помощью метода prc.terminate()
"""

import multiprocessing
import time


# def test():
#     while True:
#         print(f"{multiprocessing.current_process()}", time.ctime())
#         time.sleep(1)
#
#
# prc = multiprocessing.Process(target=test, name="prc-1")
# prc.start()
#
# print(prc.pid)
# print(prc.is_alive())
# prc.terminate() # Убивает данный процесс. Аналог sudo kill -9 <pid>

################################################################

def test_all():
    for j in range(1, 4):
        print(f"Выполнилась {j} задача процесса {multiprocessing.current_process().name}")
    time.sleep(3)


def test():
    while True:
        ...


prc = []

for i in range(3):
    process = multiprocessing.Process(target=test_all, name=f"test-{i}")
    prc.append(process)
    process.start()
    process.join()

"""
Ниже добавляем еще один процесс, который никогда не завершится
Следовательно и print(end) тоже никогда не выведется, тк есть цикл проверки на окончание процесса i,join()
"""
# pr = multiprocessing.Process(target=test)
# pr.start()
# prc.append(pr)

for i in prc:
    i.join()

print("End")
