# setattr(object, name, values)
# 给对象的属性赋值，若属性不存在，先创建再赋值。

class test():
    name = "xiaohua"

    def run(self):
        return "HelloWorld"


t = test()
# 判断属性是否存在
print(hasattr(t, "age"))
# 为属相赋值，并没有返回值
setattr(t, "age", "18")
# 属性存在了
print(hasattr(t, "age"))
