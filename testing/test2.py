import threading
import time


def get_data(data):
    for _ in range(5):
        time.sleep(1)
        print(f"{threading.current_thread().name}: {data}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(time.time(),))
thr2 = threading.Thread(target=get_data, args=(time.time(),), daemon=True)
# thr.start()
# print("Stop!")
# thr2.start()
################################################################
# thr.run()
# print("Stop!")
# thr2.start()
################################################################
thr.run()
thr2.start()
print("Stop!")

"""
Тут вся суть в том, какой это поток daemon или нет
Демон закрывается вместе с основным потоком(через небольшой промежуток времени)
Но если указывать не старт потока, а его запуск в main потоке - второй поток завершится
после выполнения первого и принта Stop
Если же оба потока запустить в соседних не main то даже если это daemon он будет исполняться
"""