class A:
    @staticmethod
    def f():
        print('static method')
    
    @classmethod
    def g(cls):
        print(cls.__name__)


if __name__ == "__main__":
    a = A()
    a.f()
    a.g()

print(type(A.f))
print(type(A.g))