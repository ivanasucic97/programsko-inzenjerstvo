Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import likovi, funkcije

k1 = likovi.Kruznica(3)
k2 = likovi.Kvadrat(5)

print('*** test program ***')
print(k1, 'opsega', funkcije.opseg(k1), 'povrsine', funkcije.povrsina(k1))
print(k2, 'opsega', funkcije.opseg(k2), 'povrsine', funkcije.povrsina(k2))
