class Account:
    def __init__(self, name, money):
        self.user = name
        #인스턴스 멤버 선언이 아니라 setter 메서드를 호출
        self.balance = money

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,money):
        if money < 0:
            return
        #실제 인스턴스 멤버 선언이 일어나는 부분
        self._balance = money
    
if __name__ == "__main__":
    my_acnt = Account("greg", 5000)
    my_acnt.balance = -3000

    # 인스턴스의 __dict__
    print(my_acnt.__dict__)

    # 클래스의 __dict__
    attr = Account.__dict__['balance']
    print(attr)
    print(hasattr(attr,'__get__'))
    print(hasattr(attr,'__set__'))
    print(hasattr(attr,'__delete__'))

    # _balance로 직접 수정하면?
    my_acnt._balance = -3000
    print(my_acnt.balance)