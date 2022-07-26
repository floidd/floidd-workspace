class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
print(th1.__dict__, '\n', '*'*30, '\n', th2.__dict__)
th1.id=2
th2.data = {'22.09.2000'}
print(th1.__dict__, '\n', '*'*30, '\n', th2.__dict__)