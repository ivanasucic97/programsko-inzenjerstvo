Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Kruznica(object):
    def __init__(self, radijus):
        self.radijus = radijus

    def __str__(self):
        return "kruznica radijusa %.2f" % (self.radijus)

class Kvadrat(object):
    def __init__(self, stranica):
        self.stranica = stranica

    def __str__(self):
        return "kvadrat stranice %.2f" % (self.stranica)

if __name__ == '__main__':
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)
