# 一种综合的用法：判断一个对象的属性是否存在，若不存在就添加该属性

class test():
    name = "xiaohua"

    def run(self):
        return "hello world"


t = test()
# age属性不存在
# print(getattr(t, "age"))
# age属性不存在时，设置该属性
print(getattr(t, "age", setattr(t, "age", "18")))
# 可检测设置成功
print(getattr(t, "age"))
