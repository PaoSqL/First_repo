# string = sir de caractere delimitate de ghilimele simple '' sau duble ""

# string
marca = 'Dacia'
model = '1301'

# int
anFabricatie = 1987;

# double/float
pret = 2300.50

# boolean
inmatriculata = False

# char
nota = 'A'

# string methods
print(marca.upper())
print(len(str(pret)))

print(pret.__le__(pret))
print(pret.__bool__())

class Person:
    def __init__(self, age):
        self.age = age
    def __le__(self, other):
        return self.age <= other.age
alice = Person(18)
bob = Person(17)
carl = Person(18)
print(alice <= bob)
# False
print(alice <= carl)
# True
print(bob <= alice)
# True