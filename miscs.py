import threading


def multithreading(function):
    t = threading.Thread(target=function)
    t.setDaemon(True)
    t.start()
