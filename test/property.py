class Account(object):
    def __init__(self, name, money):
        self.__name = name  # 帐户人姓名
        self.__balance = money  # 帐户余额

    def __get_name(self):
        return self.__name

    def set_balance(self, money):
        if isinstance(money, int):
            if money >= 0:
                self.__balance = money
            else:
                raise ValueError('输入的金额不正确')
        else:
            raise ValueError('输入的金额不是数字')

    def get_balance(self):
        return self.__balance

    # 使用 property 类来为属性设置便利的访问方式
    name = property(__get_name)
    balance = property(get_balance, set_balance)


ac = Account('tom', 10)
print(ac.name)
print(ac.balance)
ac.balance = 1000
print(ac.balance)