
import find_centers

my_list = [i for i in range(10)]

def my_func(num):
    """
    does abd

    Args:
    a (int) :does a things
    b (str) : does b things
    Returns:
    a+b (int): the sum lol
    """
    return num + 1

print(list(map(lambda x: x+1,my_list)))

print(list(filter(lambda x: x%2 == 0, my_list)))

try:
    res = range(1.0,7)
except Exception as e:
    print(f"Det er en error av type {type(e)}")

class Dings():
    def __init__(self,name, age):
        self.name = name     
        self.age = age

    def __str__(self):
        return f"dette er en dings"
    
    def funktion(self):
        print("halleo og jeg er " +self.name)

boms = Dings("potet",455)

bims = Dings("wurqhurhfu",4555545)

print(boms.name)
print(boms.age)

print(bims.name)
print(bims.age)

print(boms)

print(my_func(1,2))

boms.funktion()