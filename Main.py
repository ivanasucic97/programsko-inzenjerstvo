Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from vjezba_9.Mine.Polje import Polje


p = Polje(5,2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
        print(k, end = '|')
    print()

print('\n*** test 2 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5,2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
print(p)
