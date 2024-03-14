class Event:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def emit(self, *args, **kwargs):
        for observer in self._observers:
            observer(*args, **kwargs)
