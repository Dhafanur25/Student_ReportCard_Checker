import pprint #import fungsi untuk dictionary yang akan di print lebih rapih
daftar_CLO = {}

with open("Data_Mahasiswa.txt") as f: #membuka file txt dan memasukkan setiap line kedalam dictionary
    for line in f:
        a, b, c, d, e = str(line).split()
        daftar_CLO[a] = [b, c, d, e]

def remedial_report(NIM): #fungsi untuk cek CLO remedial
    if NIM in daftar_CLO.keys():
        for key,value in daftar_CLO.items():
            if key == NIM:
                CLO = 1
                z = 0
                print("")
                found = False
                for i in value:
                    if int(i) <= 50:
                        found = True
                        z += 1
                        if z == 1:
                            print("CLO yang remedial untuk NIM",NIM,":")
                        print("CLO {}".format(CLO))
                    CLO += 1
                if not found:
                    print("D")
                
    else:
        print("Data NIM Tidak Diketahui")

def main_program(): #fungsi untuk menjalankan program
    print("--> Program No.22 REMEDIAL <--", "(Dhafa Nur Fadhilah 1301213263)")
    print("")
    pprint.pprint(daftar_CLO)
    print("")
    print("Berikut adalah list NIM Mahasiswa:")           
    for key in daftar_CLO.keys():
        print(key)
        
    print("")
    print("{Terminate Program, Input: [EP]}")
    k = input("Silahkan input NIM mahasiswa yang ingin dicari:")
    while k != "EP":
        remedial_report(k)   
        print("")
        k = input("Input kembali NIM:")
        
    print("Terima Kasih!")
    
main_program() #memanggil fungsi main_program untuk menjalankan program
