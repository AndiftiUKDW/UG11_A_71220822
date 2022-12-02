def hitungKata(kalimat,kata):
    x = kalimat.count(kata)
    return x
def ubahKata(kalimat,terubah,perubah):
    x = kalimat.replace(terubah,perubah)
    return x
print("Pilihan Menu :")
print("1. Hitung kata")
print("2. Ubah Kata")
pilihan = int(input("Pilihan anda : "))
kalimat = str(input("Masukan sebuah kalimat/kata : "))
if pilihan == 1:
    kata = str(input("Masukan kata yang ingin dihitung : "))
    h = hitungKata(kalimat,kata)
    print("terdapat sebanyak",h,"kata",kata,"di dalam kalimat")
elif pilihan == 2:
    ubah = str(input("Masukan kata yang ingin di ubah : "))
    kataperubah = str(input("Masukan kata pengganti : "))
    h = ubahKata(kalimat,ubah,kataperubah)
    print("String berhasil dirubah menjadi :",h)
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")