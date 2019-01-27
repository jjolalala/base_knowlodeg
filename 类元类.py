class Get_Attr(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        #  选择所有不以'__'开头的属性
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        # 将它们转为大写形式
        # for name, value in attrs:
        #     if 'crawl' in name:
        #         print(name)
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        print(uppercase_attr)
        # 通过'type'来做类对象的创建
        # return super().__new__(cls, future_class_name, future_class_parents, uppercase_attr)
        # return type.__new__(cls, future_class_name, future_class_parents, uppercase_attr)
        return super(Get_Attr, cls).__new__(cls, future_class_name, future_class_parents, uppercase_attr)


class Foo(metaclass=Get_Attr):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

    def crawl_dsda(self):
        print('yiyi你好')

    def crawl_ddd(self):
        print('啦啦啦')


p = Foo()
p.CRAWL_DDD()