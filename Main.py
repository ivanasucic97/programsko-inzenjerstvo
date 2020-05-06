Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from vjezba6.Ispit import Ispit
from vjezba6.IspitDB import IspitiDB

print("ZADATAK 6.1")

isp = Ispit()
isp.dodaj("Ante Anti�", "Linearna algebra", 5)
isp.dodaj("Ante Anti�", "Programiranje 1", 4)
isp.dodaj("Marija Mariji�", "Linearna algebra", 4)
isp.dodaj("Marija Mariji�", "Matemati�ka analiza", 5)

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

db.dodaj_student("Ante Anti�")
db.dodaj_student("Ana Ani�")
db.dodaj_student("Pero Peri�")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Peri�"))
print(db.vrati_student_id("Marija Mariji�"))

db.izbrisi_student("Pero Peri�")
db.promijeni_student("Ana Ani�","Marija Mariji�")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

print("---------------------------------------------------------------------")

print("\nZADATAK 6.4")

print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Anti�")
db.dodaj_student("Marija Mariji�")
db.dodaj_kolegiji("Linearna algebra")
db.dodaj_kolegiji("Programiranje 1")
db.dodaj_kolegiji("Matemati�ka analiza")
db.ispitaj("Ante Anti�", "Linearna algebra", 5)
db.ispitaj("Ante Anti�", "Linearna algebra", 3)
print(db.svi_ispiti())
db.ispitaj("Ante Anti�","Linearna algebra",4)
print(db.svi_ispiti())
db.ispitaj("Ante Anti�","Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Anti�","Linearna algebra",5)
db.ispitaj("Marija Mariji�","Programiranje 1",5)
db.ispitaj("Marija Mariji�","Matemati�ka analiza",4)
print(db.svi_ispiti())

print("---------------------------------------------------------------------")
