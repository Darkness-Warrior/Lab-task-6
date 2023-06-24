def sizer(cls):
    class SizedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            try:
                self.size = len(self)
            except TypeError:
                try:
                    self.size = abs(self)
                except TypeError:
                    self.size = 0
    print("Оно живое!")
    return SizedClass


@sizer
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

my_object = MyClass(1,2)
print(my_object.size) 
