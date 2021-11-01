print("------------------------------")
print("         Melody Cafe            ")
print("           kasir A              ")
print("       Nama kasir = Naya        ")
print("------------------------------")
pelanggan =input ("Nama Pelanggan: ")
hari = str(input ("pilih hari: \n A. Weekdays\nB. Weekend:\n "))


pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    cafe melody          
    List Menu
 
    ==============================
    A. Nasi goreng  :  Rp 15.000
    B. Ayam kremes  :  Rp 17.000
    C. Mie ayam  :  Rp 13.000
    D. Bakso  :  Rp 13.000
    E. Soto ayam  :  Rp 12.000
    F. Es Teh  :  Rp 5.000
    G. Teh hangat  :  Rp 5.000
    H. Es Jeruk  :  Rp 7.000
    I. Jeruk hangat  :  Rp 7.000
    J. Air mineral  :  Rp 4.000
    ==============================
    """)


    pesan=str(input("masukkan list abjad menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Nasi goreng"
        harga=(15000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "b":
        listnama= " Ayam kremes"
        harga = (17000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "c":
        listnama= "Mie ayam"
        harga = (13000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "d":
        listnama= "Bakso"
        harga = (13000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "e":
        listnama= "Soto ayam"
        harga = (12000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "f":
        listnama= "Es Teh"
        harga = (5000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "g":
        listnama= "Teh hangat"
        harga = (5000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "h":
        listnama= "Es Jeruk"
        harga = (7000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "i":
        listnama= "Jeruk hangat"
        harga = (7000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "j":
        listnama= "Air mineral"
        harga = (4000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")

    pembayaran = str(input("Pembayaran melalui : \na. Cash\nb. E-money: \n "))
    if pembayaran =="b":
        diskonpay = totalharga*0.1
        totalharga = totalharga - diskonpay
    else:
        diskonpay = (0)
        totalharga = totalharga

    if hari == "a":
        diskonhari = totalharga*0.1
        totalharga = totalharga - diskonhari
    else :
        diskonhari = totalharga*0.05
        totalharga = totalharga - diskonhari

    print("--------------------------")
    print("Melody Cafe")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("Diskon Pembayaran :", diskonpay)
    print("Diskon hari pembelian :", diskonhari)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("Terima kasih!")
    print("--------------------------")

    pilihan=input("apakah anda ingin order kembali Y/N =")
