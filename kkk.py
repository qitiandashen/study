class Dog(object):
    def __init__(self,name):
           self.name = name

    def eat(self,food):
        print("%s is eating..." %self.name,food)

d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):
    func = getattr(d,choice)
    func("ChenRongHua")
