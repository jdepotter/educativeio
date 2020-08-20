import Foo 

ANIMAL = 'Tiger'

def value2(self):
    print(ANIMAL)

Foo.Bar.value2 = value2


bar = Foo.Bar()
bar.value1()
bar.value2()

