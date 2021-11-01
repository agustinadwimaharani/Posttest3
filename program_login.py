def login(name,password):
    sukses = False
    file = open("logindatabase.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             sukses = True
             break
    file.close()
    if(sukses):
        print("-"*40)
        print("  | Login Berhasil, silahkan masuk  | ")
        print("-"*40)
    else:
        print("-"*50)
        print("   | Anda belum terdaftar, silahan register  | ")
        print("-"*50)

i=3
while i>=1:
    userName_=input("masukan username anda :")
    password_=input("masukan password :")
    hasil=(login(userName_, password_))
    if hasil == True:
        print ("login user berhasil")
        break
    else :
        i-=1
        print("gagal login, sisa percobaan login adalah :", i )
        
def register(name,password):
    file = open("logindatabase.txt","a")
    file.write("\n"+name+","+password)
def access(option):
    global name
    if(option=="login"):
        name = input("Masukkan ID: ")
        password = input("Masukkan Password: ")
        login(name,password)
    else:
        print(" | Masukkan ID dan Password baru anda! | ")
        name = input("Masukkan ID : ")
        password = input("Masukkan password anda: ")
        register(name,password)
        print(" | Register anda berhasil, silahkan masuk | ")

def begin():
    global option
    print("="*45)
    print(" |  Selamat datang di kara program login  |")
    print("-"*45)
    print("Ketik 'login' jika anda sudah punya akun")
    print("Ketik 'reg' jika anda belum memiliki akun")
    print("="*45)
    option = input("slahkan masukkan (login/reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

