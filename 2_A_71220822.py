def cetakHuruf(huruf):
    x = len(huruf)
    if(x%2==0):
        kanan = huruf[0:3]
        kiri = huruf[x-3:x]
        b = kanan+" dan "+kiri
    else:
        nt= int((x/2)-1)
        tengah = huruf[nt:nt+3]
        b = tengah
    return b
    
kata = str(input("Masukan kata : "))
hasil = cetakHuruf(kata)
print("Huruf yang diambil pada kata",kata,"adalah",hasil)