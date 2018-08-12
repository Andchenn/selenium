class myclass(object):
    value = 10

    def act(self):
        print('This is a test.')

    @staticmethod
    def smeth():
        print('This is a static method.')
        # 类名.属性名
        print(myclass.value)
        # 类名.方法名
        print(myclass.act)

    @classmethod
    def cmeth(cls):
        print('This is a class method of ', cls)
        # 参数访问类的属性
        print(cls.value)
        # 参数访问类的方法
        print(cls.act)


myclass.smeth()
myclass.cmeth()
my = myclass()
my.cmeth()
my.smeth()
