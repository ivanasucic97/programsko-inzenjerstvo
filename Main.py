Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from vjezba6.Ispit import Ispit
from vjezba6.IspitDB import IspitiDB

print("ZADATAK 6.1")

isp = Ispit()
isp.dodaj("Ante Antiæ", "Linearna algebra", 5)
isp.dodaj("Ante Antiæ", "Programiranje 1", 4)
isp.dodaj("Marija Marijiæ", "Linearna algebra", 4)
isp.dodaj("Marija Marijiæ", "Matematièka analiza", 5)

isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt", encoding="utf8").read())

isp = Ispit.ucitaj_datoteku("ispiti.txt")
print(isp)

print("---------------------------------------------------------------------")

print("\nZADATAK 6.2")

isp.spremi_json("ispiti.json")
print(open("ispiti.json", encoding="utf8").read())
Ispit.ucitaj_json("ispiti.json")
print(isp)

print("---------------------------------------------------------------------")

print("\nZADATAK 6.3")

print('*** TEST SQLite studenti ***')
db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

db.dodaj_student("Ante Antiæ")
db.dodaj_student("Ana Aniæ")
db.dodaj_student("Pero Periæ")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Periæ"))
print(db.vrati_student_id("Marija Marijiæ"))

db.izbrisi_student("Pero Periæ")
db.promijeni_student("Ana Aniæ","Marija Marijiæ")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

print("---------------------------------------------------------------------")

print("\nZADATAK 6.4")

print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antiæ")
db.dodaj_student("Marija Marijiæ")
db.dodaj_kolegiji("Linearna algebra")
db.dodaj_kolegiji("Programiranje 1")
db.dodaj_kolegiji("Matematièka analiza")
db.ispitaj("Ante Antiæ", "Linearna algebra", 5)
db.ispitaj("Ante Antiæ", "Linearna algebra", 3)
print(db.svi_ispiti())
db.ispitaj("Ante Antiæ","Linearna algebra",4)
print(db.svi_ispiti())
db.ispitaj("Ante Antiæ","Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antiæ","Linearna algebra",5)
db.ispitaj("Marija Marijiæ","Programiranje 1",5)
db.ispitaj("Marija Marijiæ","Matematièka analiza",4)
print(db.svi_ispiti())

print("---------------------------------------------------------------------")
