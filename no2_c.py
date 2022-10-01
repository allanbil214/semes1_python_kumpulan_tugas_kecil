barang = {0: {"barang":"Pensil","qty":10,"satuan":"Pcs","harga":5000},
          1: {"barang":"Buku","qty":10,"satuan":"Pcs","harga":4000},
          2: {"barang":"Minyak Goreng","qty":10,"satuan":"Ltr","harga":15000},
          3: {"barang":"Gula","qty":5,"satuan":"Kg","harga":6000}}

thotty = 0

def showBody():
    global thotty
    for anu in range(len(barang)): 
        nb = barang[anu]
        amount = nb["harga"] * nb["qty"]    
        if(anu == 2):
            print(nb["barang"], "\t ", 
                  nb["qty"],  
                  nb["satuan"], "\t\t", 
                  nb["harga"],  "\t\t", 
                  amount)
        elif(anu == 3):
            print(nb["barang"], "\t\t\t  ", 
                  nb["qty"],
                  nb["satuan"], "\t\t ", 
                  nb["harga"], "\t\t ", 
                  amount)
        else:
            print(nb["barang"], "\t\t\t ", 
                  nb["qty"],  
                  nb["satuan"], "\t\t ", 
                  nb["harga"], "\t\t ", 
                  amount)    
        
        thotty += amount

print()
print("DAFTAR BELANJA")
print("======================================================")
print("Barang\t \t \t", "QTY", "Satuan\t\t", "Harga\t", "Jumlah Harga")
print("======================================================")
showBody()
print("======================================================")
print("Total \t\t\t\t\t\t\t\t\t\t", thotty)
print("======================================================")
