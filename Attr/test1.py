# hasattr(object, name)
# 判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
# 需要注意的是name要用括号括起来

class test():
    name = "xiaohua"

    def run(self):
        return "Hello World"


t = test()
print(hasattr(t, "name"))
print(hasattr(t, "run"))
