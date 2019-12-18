import threading


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, func, timer, num_min, num_max):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.func = func
        self.timer = timer
        self.num_min = num_min
        self.num_max = num_max

    def run(self):
        self.func(self.name, self.timer, self.num_min, self.num_max)
