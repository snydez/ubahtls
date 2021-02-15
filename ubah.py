#!/usr/bin/env python3

def posisikonsonan(strKata, intPos):
    z = 0
    counterPos = 0
    while z < len(strKata):
        if strKata[z] not in konsonan:
            z=z+1
        else:
            counterPos = counterPos+1
            if counterPos == intPos:
                break
            else:
                z=z+1

        if z>=len(strKata):
            #gak ada konsonan di kata ini
            z=-99
            break

    return z


def ubahhuruf(strKata, posisiHuruf, jadiHuruf):
    #pecah kata jadi perhuruf
    pecahHuruf = list(strKata)
    pecahHuruf[posisiHuruf] = jadiHuruf

    return "".join(pecahHuruf)


def tukarHurufdariKata(kata1,kata2, arah):
    #tukar huruf dari masing masing kata
    if arah=="2ke1":
        #tukar kata
        katax = kata1
        kata1 = kata2
        kata2 = katax

    poskonsKata1 = posisikonsonan(kata1, 2)
    poskonsKata2 = posisikonsonan(kata2, 1)
    hasilubahkata = ""

    try:
        if arah=="1ke2":
            hasilubahkata = ubahhuruf(kata1, poskonsKata1, kata2[poskonsKata2])
        elif arah=="2ke1":
            hasilubahkata = ubahhuruf(kata2, poskonsKata2, kata1[poskonsKata1])
        else:
            hasilubahkata = "[error]"

    except:
        print(kata1 + "; " + kata2 + "; poskonsKata1 =" + str(poskonsKata1) + "; poskonsKata2 = " + str(poskonsKata2))
        if arah=="1ke2":
            hasilubahkata = kata1
        if arah=="2ke1":
            hasilubahkata = kata2

    return hasilubahkata


untukdiubah = list("")
f = open("untukdiubah.txt","r")
tulisan = f.read()

potong = tulisan.split(" ")

vocall = {'a','u','i','e','o','y'}
konsonan = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}

print(tulisan)

n=0
kataterganti = []
strKata1 = potong[n]
strKata2 = potong[n+1]

print("jumlah kata= " + str(len(potong)))
while True:
    katapertama = tukarHurufdariKata(strKata1,strKata2,"1ke2")
    katakedua = tukarHurufdariKata(strKata2, strKata1,"2ke1")
    print(str(n) + " kata1=" + strKata1 +";" + katapertama + "  kata2=" + strKata2 + ";" + katakedua )

    kataterganti.append(katapertama)

    n=n+1
    strKata1 = katakedua


    if n> len(potong)-2:
        break
    else:
        strKata2 = potong[n+1]

kataterganti.append(katakedua)
kalimatterganti = " ".join(kataterganti)

print(kalimatterganti)

fw = open("hasilubah.txt","w")
fw.write(kalimatterganti)
fw.close()
