class A:
    def __init__(self, a, b, c=33):
        self.w = a
        self.h = b
        self.d = 3
        self.c = c


class B(A):
    def __init__(self):
        super().__init__(a.w, a.h, a.c)  # или в данном случае A.__init__(self)
        self.d = a.d + 20

    def op(self):
        self.r = a.w + 300
        return self.r, a.c


a = A(1, 2)
b = B()
print(b.w, a.d, b.h, b.c, b.d, b.op())
