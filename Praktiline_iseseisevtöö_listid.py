from string import * 

#1
vokaali=["a","e","u","o","i","ü","ö","ä"]
konsonanti="qwrtpsdfghklzxcvbnmj"
markid=punctuation
v=k=m=t=0
tekst=input("Sisesta sõna või laus: ").lower() #"ABCD"->"abcd!"
tekst_list=list(tekst) #["a","b","c","d","!"]
for sümbol in tekst_list:
    if sümbol in vokaali:
        v+=1
    elif sümbol in konsonanti:
        k+=1
    elif sümbol in markid:
        m+=1
    elif sümbol==" ":
        t+=1
print("Vokaali:",v)
print("Konsonanti:",k)
print("Kirjuvahemärgid:",m)
print("Tühikud:",t)
#2

# Küsi kasutajalt viis nime
nimed = []
for i in range(5):
    nimi = input("Sisestage nimi: ").capitalize()
    nimed.append(nimi)

# Kuva nimed tähestikulises järjekorras
print("Nimed tähestikulises järjekorras:")
nimed.sort()
print(nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")


# Kuva viimati lisatud nimi
print("Vimasena oli lisatud: ",nimi)
# Lisa võimalus muuta loendis olevaid nimesid
print("Kas soovite muuta loendis olevaid nimesid?")
muuda = input("Jah või Ei: ")
if muuda.lower() == "jah":
    indeks = int(input("Sisestage muudetava nime indeks: "))
    uus_nimi = input("Sisestage uus nimi: ")
    nimed[indeks] = uus_nimi
    print("Nimed pärast muutmist:", nimed)
# Tekita loend ilma kordusteta
uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

uued_nimed=list(set(nimed))
# Loo vanuste loend
vanused = [25, 30, 22, 35, 40]
# Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
max_vanus = max(vanused)
min_vanus = min(vanused)
kogusumma = sum(vanused)
keskmine_vanus = kogusumma / len(vanused)
print("Suurim vanus:", max_vanus)
print("Väikseim vanus:", min_vanus)
print("Kogusumma:", kogusumma)
print("Keskmine vanus:", keskmine_vanus)

 