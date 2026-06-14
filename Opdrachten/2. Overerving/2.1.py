# Wat is de output van deze code?
#
# A: De applicatie gooit een error
# B: Max Verstappen
#    FIA Super Licence
# C: FIA Super Licence
#    Max Verstappen

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Racer(Person):
    def __init__(self, name, certificate):
        super().__init__(name)
        self.__certificate = certificate

    def print_certificate(self):
        print(self.__certificate)

racer = Racer("Max Verstappen", "FIA Super Licence")
print(racer.get_name())
racer.print_certificate()
