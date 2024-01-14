class ClassStudent:
    def __init__(self, name, major, gpa, probation):
        self.a = name
        self.b = major
        self.c = gpa
        self.d = probation

    def honor(self):
        if self.c >= 3.5:
            return True
        else:
            return False

    @classmethod
    def prints(cls):
        print("This is the class method")
