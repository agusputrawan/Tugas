print( "-" *5 + " GUNTING KERTAS BATU ABANGKUHHH !!! " + "-"*5)
pemain_1 = input("Pemain 1 bernama ")
pemain_2 = input("Pemain 2 bernama ")

print("")
print( "-" *5 + " Peraturan permainnya " + "-" *5 )
print(" ketiklah angka untuk kemenangan ")

gunting = print('1. gunting')
kertas = print('2. kertas')
batu = print('3. batu')

print("")
opsi_satu = int(input(f"Masukkan nomor pilhan sepuh {pemain_1} "))
opsi_dua = int(input(f"Ampun segini nomor saya puh  {pemain_2} "))

def permainan(opsi_satu, opsi_dua):
    if opsi_satu == opsi_dua:
        print("Wah sepuh bisa aja")
    elif (opsi_satu == 3 and opsi_dua == 1) or \
         (opsi_satu == 2 and opsi_dua == 3) or \
         (opsi_satu == 1 and opsi_dua == 2) : 
        print(f"{pemain_1} sepuh memang jago!")
    else:
        print(f"{pemain_2} cuma hoki puh")

permainan(opsi_satu,opsi_dua)
        
    
