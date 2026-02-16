class A:
    c_mem = 10 #클래스 멤버

    @classmethod    
    def cls_f(cls): #클래스 메서드
        print(cls.c_mem)

    def __init__(self,num): #인스턴스 초기화
        self.i_mem = num

    def ins_f(self): #인스턴스 메서드
        print(self.i_mem)

if __name__ == "__main__":
    print(A.c_mem)
    A.cls_f()

    a = A(20)
    print(a.c_mem)
    a.cls_f()