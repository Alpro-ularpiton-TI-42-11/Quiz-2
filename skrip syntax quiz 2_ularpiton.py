saldo = 1500000
pin = int(input("Masukkan Nomor PIN : "))

print("Selamat datang di Link.aja")
print("\nMenu Layanan\n1.Transaksi\t2. Cek Saldo")
menu=int(input("Pilih Menu : "))

if menu ==1:
    print("\nPilih Transaksi yng diinginkan") 
    print("1. Debit\t2. Kredit")
    menu_1=int(input("Transaksi : "))

    if menu_1 ==1:
        setor=float(input("Jumlah uang yang disimpan : Rp. "))
        saldo_1=saldo+setor
        print("Selamat saldo anda bertambah menjadi = ", saldo_1)
    if menu_1 ==2:
        tarik=float(input("Jumalah uang yang ditarik : Rp. "))
        saldo_2=saldo-tarik
        
        if saldo > tarik:
            print("Transaksi Berhasil\nSisa saldo anda : ", saldo_2)
        if saldo < tarik:
            print("Saldo anda tidak mencukupi")
            

if menu ==2:
    print("Sisa Saldo anda : Rp. ", saldo)