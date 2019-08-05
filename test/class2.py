class A(object):
    a = 1

    def instance_method(self):
        print('实例方法打印类变量a: %s' % self.a)

    @classmethod
    def class_method(cls):
        print('类方法打印类变量a: %s' % cls.a)

    @staticmethod
    def static_method(b):
        print('静态方法打印自己的变量b: %s' % b)


# A.instance_method()  # 报错
A().instance_method()  # 实例方法打印类变量a: 1

A.class_method()  # 类方法打印类变量a: 1
A().class_method()  # 类方法打印类变量a: 1

A.static_method(12)  # 静态方法打印自己的变量b: 12
A().static_method(12)  # 静态方法打印自己的变量b: 12
