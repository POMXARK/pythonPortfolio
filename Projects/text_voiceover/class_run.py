class Class_run():

    def __init__(self, **kwargs): # выполняется при вызове класса , можно добавлять свои аргументы (переменные)
        super(Class_run, self).__init__(**kwargs) # обязательно
        self.run_def = False