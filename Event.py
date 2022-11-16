class Event:
    def __init__(self):
        self.__listener_list = []

    def add_listener (self, callback):
        self.__listener_list.extend(callback)

    def remove_listener (self, callback):
        self.__listener_list.remove(callback)

    def remove_all_listener (self):
        self.__listener_list.clear()

    def invoke (self, *args):
        for callback in self.__listener_list:
            callback(*args)