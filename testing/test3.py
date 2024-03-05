"""Про Lock и RLock
Если вкратце - блокировать поток мы можем при помощи threding.Lock.acquire()
Разблокировать мы можем при помощи threding.Lock.release() из любого потока, текущего, main или другого
В случае с Rlock.acquire() мы можем разблокировать исполнение только из текущего потока """
import threading

locker = threading.Lock()


def get_lock():
    print(f"Блокировка из текущего потока: {threading.current_thread().name}")
    locker.acquire()
    """
    Этот метод у класса Lock блокирует дальнейшее исполнение кода, пока поток не будет разблокирован
    Поток можно разблокировать из любого места при помощи release()
    """
    print(f"Поток разблокирован: {threading.current_thread().name}")

    """
    release разблокирует поток для остальных
    Lock.release() может разблокировать поток из любого потока
    """


thr1 = threading.Thread(target=get_lock)
thr2 = threading.Thread(target=get_lock)

thr1.start()
thr2.start()

locker2 = threading.RLock()


def get_lock2():
    print(f"Блокировка поток из текущего: {threading.current_thread().name}")
    locker2.acquire()
    print(f"Поток разблокирован: {threading.current_thread().name}")


thr3 = threading.Thread(target=get_lock2)
thr4 = threading.Thread(target=get_lock2)

thr3.start()
thr4.start()


"""
Для интерактивного управления python3 -i testing/test3.py
"""