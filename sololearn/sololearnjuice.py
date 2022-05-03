class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        return Juice(self.name + "&" + other.name, str(self.capacity + other.capacity))


c = str(input())
cn = float(input())
t = str(input())
tn = float(input())
a = Juice(c, cn)
b = Juice(t, tn)

result = a + b
print(result.name + "(" + result.capacity + "L)")
