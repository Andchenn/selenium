class method(object):
    value = 999

    def __init__(self, data):
        self.data = data

    def instance_method(self):
        print(self.data)

    @staticmethod
    def static_method():
        print("This is static method.")

    @classmethod
    def class_method(cls):
        print(cls.value)


m = method(10)
m.instance_method()
m.static_method()
m.class_method()
# 不用实例化
method.static_method()
method.class_method()