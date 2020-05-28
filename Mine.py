Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pprint import pprint

class Kvadrat():

    '''
    Stvori datoteku mine.py Implementiraj klasu Kvadrat i u njoj metodu __init__().
    Prilikom inicijalizacije kvadrata postavljaju se privatni atributi __broj na preneseni broj, __otkriven na False i __oznaka na False.
    Implementiraj metodu otkrij() koja æe otkriti kvadrat ako nije oznaèen.
    Implementiraj metodu oznaci() koja æe oznaèiti kvadrat ako nije otkriven, ili skinuti oznaku ako je kvadrat veæ oznaèen.
    Implementiraj metode kao svojstva jeMina(), jeBroj() i jePrazan() koje æe vratiti True ili False ako je kvadrat mina, broj ili prazan.
    '''


    def __init__(self, broj = 0):
        self.__broj = broj
        self.__otkriven = False
        self.__oznaka = False

    def otkrij(self):
        if self.__otkriven == False:
            self.__otkriven = True

    def oznaci(self):
        if self.__oznaka == False:
            self.__oznaka = True
        else:
            self.__oznaka = False

    @property
    def jeMina(self):
        if self.__broj == -1:
            return True
        return False

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def broj(self):
        return self.__broj

    @property
    def jePrazan(self):
        if self.__broj == 0:
            return True
        return False

    '''
    Implementiraj stringovnu reprezentaciju __str__() koja æe vratiti: 
        toèku '.' ako kvadrat nije otkriven 
        upitnik '?' ako je kvadrat oznaèen 
        križiæ 'x' ako je kvadrat otkriven i sadrži minu 
        broj 'n' gdje je n broj ako je kvadrat otkriven i sadrži broj 
        razmak ' ' ako je kvadrat otkriven i ako je prazan
    '''

    def __str__(self):
        if self.__otkriven == False:
            return "."
        elif self.__oznaka == True:
            return "?"
        elif self.__otkriven == True and self.__broj == -1:
            return "x"
        elif self.__otkriven == True and self.__broj > 0:
            return str(self.__broj)
        elif self.__otkriven == True and self.__broj == 0:
            return " "
