from argparse import Action
from asyncio.windows_events import NULL
from fileinput import close
from pickle import FALSE, TRUE
from tkinter import Variable

#Fungsi Keyakinan
def yakin(message):
    sure = input('Apakah Anda Yakin untuk '+ message.capitalize()+' (Y/N)? ').lower()
    if(sure== 'y' or sure == 'yes'):
        return TRUE
    elif(sure == 'n' or sure == 'no'):
        return FALSE
    else:
        return yakin(message)

#Fungsi Cek NIM
def checknim():
    nim = input('Masukkan NIM : ')
    banyakdata = len(data)
    index = 0
    for i in range(banyakdata):
        if(int(nim) == int(data[i]['nim'])):
            index += i+1
        else:
            index +=0
    return index

#Fungsi READ
def allReport():
    banyakData = len(data) 
    if(banyakData != 0):
        print('-------------------------------------------------')
        print('| No  | NIM |   NAMA    |   GENDER  |   KOTA   |')
        for i in range(banyakData):
            print('| ', i+1, ' | ', data[i]['nim'],' |  ', data[i]['nama'], '   | ', data[i]['gender'], '    | ', data[i]['kota'], ' |')
        print('-------------------------------------------------')
    else:
        print('Belum ada data siswa dalam database')
        show()
def singleReport():
    index = checknim()
    if(index!= NULL):
        print('NIM    :', data[index-1]['nim'])
        print('Nama   :', data[index-1]['nama'])
        print('Gender :', data[index-1]['gender'])
        print('Kota   :', data[index-1]['kota'])
        print('')
    else:
        print('Tidak ada data dengan nim tersebut')
        singleReport()              
def show():
    print('''======= Report Data Siswa =======

    1. Report Seluruh Data
    2. Report Data Tertentu
    3. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Report Data Siswa [1 - 3] : ')
    if code == '1':
        allReport()
    elif code == '2':
        singleReport()
    elif code == '3':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        show()

#Fungsi DELETE
def deletedata():
    index = checknim()
    if(index!= NULL):
        jawaban = yakin('Hapus Data')
        if(jawaban == TRUE):
            del data[index-1]
            print('Data telah terhapus')
        else:
            delete()        
    else:
        print("Tidak ada data dengan nim tersebut")
        delete() 
def delete():
    print('''======= Menghapus Data Siswa =======

    1. Hapus Data Siswa
    2. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Delete Data [1 - 2]')
    if code == '1':
        deletedata()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        delete()

#Fungsi CREATE/ADD
def adding():
    banyakdata = len(data)
    print('Menambah Data Baru')
    nimbaru = int(input('Masukkan NIM : '))
    namabaru = input('Masukkan Nama : ').capitalize()
    genderbaru = input('Masukkan Gender : ').capitalize()
    kotabaru = input('Masukkan Kota : ').capitalize()
    jawaban = yakin('Menambah Data')
    if(jawaban==TRUE):
        data.append({'nim':nimbaru, 'nama':namabaru, 'gender':genderbaru, 'kota':kotabaru})
        print('Data berhasil ditambah')
    else:
        add()
def add():
    print('''======= Menambah Data Siswa =======

    1. Tambah Data Siswa
    2. Kembali Ke Menu Utama

    ''')
    code = input('Silahkan Pilih Sub Menu Menambah Data Siswa [1 - 2] : ')
    if code == '1':
        adding()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        add()

#Fungsi UPDATE/EDIT
def editdata():
    index = checknim()
    if(index!= NULL):
        kolom = input('Masukkan kolom yang ingin diedit : ').lower()
        keys = data[0].keys()
        var=0
        for j in keys:
            if(j==kolom):
                var += 1
            else:
                var += 0
        if(var!=0):
            baru = input('Masukkan '+ kolom.capitalize()+' Baru : ')
            jawaban = yakin('Edit Data')
            if(jawaban == TRUE):
                data[index-1][kolom] = baru
                print('Data telah terupdate')
            else:
                edit()            
        else:
            print('Tidak ada nama kolom tersebut')
            edit()    
    else:
        print("Tidak ada data dengan nim tersebut")
        edit() 
def edit():
    print('''======= Mengubah Data Siswa =======

    1. Ubah Data Siswa
    2. Kembali Ke Menu Utama

    ''')

    code = input('Silahkan Pilih Sub Menu Mengubah Data Siswa [1 - 2] : ')
    if code == '1':
        editdata()
    elif code == '2':
        menu()
    else :
        print('*** Pilihan yang anda masukkan salah ***')
        edit()

#Fungsi EXIT
def close():
    jawaban = yakin('Keluar dari Aplikasi')
    if(jawaban==TRUE):
        print('Terima Kasih')
        exit()
    else:
        menu()

#Default MENU
def menu():
    print('''======= Data Record Siswa Purwadhika =======

        1. Report Data Siswa
        2. Menambahkan Data Siswa
        3. Mengubah Data Siswa
        4. Menghapus Data Siswa
        5. Exit
        ''')

    code = input('Silahkan Pilih Main Menu [1-5] : ')
    if code == '1':
        show()
    elif code == '2':
        add()
    elif code == '3':
        edit()
    elif code == '4':
        delete()
    elif code == '5':
        close()
    else :
        print('  *** Pilihan yang anda masukkan salah ***')

data = [
    {
        'nim': 1,
        'nama':'Andi',
        'gender': 'Pria',
        'kota': 'Palembang'
    },
    {
        'nim': 2,
        'nama':'Budi',
        'gender': 'Pria',
        'kota': 'Jakarta'
    },
    {
        'nim': 3,
        'nama':'Cika',
        'gender': 'Wanita',
        'kota': 'Bandung'
    }
]

while(True):
    menu()
