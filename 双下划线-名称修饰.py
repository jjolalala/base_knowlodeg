# _ManglingTest__mangled='HUKAKA'


class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

        '''
        双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突（名为名称修饰）适应于变量与类方法
        ，例如__mangled会被修饰为_ManglingTest____mangled，
        前导下划线仅仅是一个约定。 给程序员一个提示而已
        '''

    def __get_mangled(self):
        return "你好"


if __name__ == '__main__':
    r = ManglingTest()

    '''
    对比常规访问访问与名称修饰访问
    '''
    # print(r.__mangled)
    print(r._ManglingTest__mangled)
    # print(r.__get_mangled())
    print(r._ManglingTest__get_mangled())