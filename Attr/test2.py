# getattr(object, name[,default])
# 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
# 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
# 可以在后面添加一对括号

class test():
    name = "xiaohua"

    def run(self):
        return "Hello World"


t = test()
# 获取name属性，存在就打印出来
print(getattr(t, "name"))
# 获取run方法，存在就打印出方法的内存地址
print(getattr(t, "run"))
# 获取run方法，后面加括号可以将方法运行
print(getattr(t, "run")())
# 获取一个不存在的属性
# print(getattr(t, "age"))
# 若属性不存在，返回一个默认值
print(getattr(t, "age", "18"))
