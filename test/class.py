class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"  # 实例变量，属性

    def make_cake(self):  # 实例方法，方法
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class Prentice(Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"

    def make_cake(self):
        self.__init__()  # 执行本类的__init__方法，做属性初始化 self.kongfu = "猫氏...."
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def make_old_cake(self):
        # 方式1. 指定执行父类的方法
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法2. super() 带参数版本
        super(Prentice, self).__init__() # 执行父类的 __init__方法
        super(Prentice, self).make_cake()

        # 方法3. super()的简化版，只支持新式类
        # super().__init__()  # 执行父类的 __init__方法
        # super().make_cake()  # 执行父类的 实例方法


damao = Prentice()
damao.make_cake()
damao.make_old_cake()