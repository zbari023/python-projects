# my fist class that give you which number is bigger
class Maximum:
    print("Max of 2 values: ")
    x = int(input("enter your first number: "))
    y = int(input("enter your secund number: "))

    def __init__(self):
        self.myfunc(None, None)

    def myfunc(self, x, y):
        if self.x > self.y:
            print("x is bigger than y")
        elif self.x == self.y:
            print("x equal y")
        else:
            print("y is bigger than x")

Maximum()
