class D():
    def printt(self):
        return "3"

class A(D):
    def print(self):
        return "1"

class B():
    def printt(self):
        return "2"

class C(A, B):
    def __init__(self):
        print("1")
        print("______------")



c1 = C()
print(c1.printt())
