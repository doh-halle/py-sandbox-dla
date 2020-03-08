class Mammal:
    def walks(self):
        print("walk")


class Dog(Mammal):
    def barks(self):
        print("Barks - Woof Woof!!")


class Cat(Mammal):
    def purss(self):
        print("Purss")

cat1 = Cat()
cat1.walks()