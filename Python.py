fachri = str(input("masukkan pilihan fachri : "))
alin = str(input("masukkan pilihan alin : "))

if (fachri == "batu" and alin == "gunting"):
    print ("fachri menang!")
elif (fachri == "batu" and alin == "batu"):
    print ("seri")
elif (fachri == "gunting" and alin == "kertas"):
    print ("fachri menang!")
elif (fachri == "gunting" and alin == "gunting"):
    print ("seri")
elif (fachri == "kertas" and alin == "kertas"):
    print ("seri")
elif (fachri == "kertas" and alin == "gunting"):
    print ("alin menang!")
elif (fachri == "batu" and alin == "kertas"):
    print ("alin menang!")
elif (fachri == "kertas" and alin == "batu"):
    print ("fachri menang!")
elif (fachri == "gunting" and alin == "batu"):
    print ("alin menang!")
else:
    print ("masukkan inputan yang benar!")



    bilangan = int(input("masukkan suatu bilangan ganjil/genap : "))
if bilangan %2 == 0:
    print("adalah bilangan genap")
else:
    print("adalah bilangan ganjil")



    bilangan = float(input("masukkan suatu bilangan negatif/positif : "))
if bilangan < 0:
    print("bilangan ini adalah bilangan Negatif")
elif bilangan > 0:
    print("bilangan ini adalah bilangan Positif")
else:
    print("bilangan ini adalah nol")



