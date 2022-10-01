def mainDef():

    print("\n#=========================================================================#")
    print("|i| Tekan Tombol [y] kemudian [Enter] jika ingin melakukan konversi")
    print("|i| Tekan tombol [n] kemudian [Enter] jika ingin membatalkan dan keluar")
    print("#=========================================================================#")
    inpChoice = input("|=| Pilih Perintah : ")
    
    if (inpChoice == "y"):
        print("\n|i| Pilih angka dari 0 sampai 100")
        inpNum = input("|=| Masukkan Angka : ")
        offspring = convertDef(inpNum)
        checkCount = len(offspring)
        if (checkCount > 3):
            print('\n|i| Output : ' +offspring.replace("Nol", ""))
        elif (checkCount == "Nol"):
            print ('\n|i| Output : ' +offspring)
    elif (inpChoice == "n"):
        print("\n|!| Good Bye!")
        return
    else:
        print("\n|!| Beep Boop Pilihan Input Salah!")
    mainDef()
    
def convertDef(vNum):
    arrNum = ["Nol","Satu","Dua","Tiga","Empat","Lima","Enam",
              "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    output = " "
    baseNum = int(vNum)
    if baseNum>= 0 and baseNum <= 11:
        output = arrNum[baseNum]
    elif baseNum <20:
        output = convertDef(baseNum-10) + " Belas "
    elif baseNum <100:
        output = convertDef(baseNum/10) + " Puluh " + convertDef(baseNum%10)    
    else:
        print("\n|!| Beep Boop Salah Input!")
    return output

mainDef()