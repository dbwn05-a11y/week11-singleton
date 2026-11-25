class SingletonCounter:
    __instance = None

    def __new__(cls):
        raise TypeError("SingletonCounter.get_instance()를 사용하세요.")

    @classmethod
    def get_instance(cls):
        # 처음 요청할 때만 객체를 만들고 카운터를 초기화한다.
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.count = 0
        return cls.__instance

    def increment(self):
        self.count += 1
