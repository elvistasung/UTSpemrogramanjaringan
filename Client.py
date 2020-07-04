# mengirimkan kembali pesan ke client
client.send(balik)

# menutup client
client.close()

# menutup socket
s.close()

# !/usr/bin/env python

# impor modul socket
import socket

# menentukan alamat server
server_address = ('localhost', 4999)

# ukuran buffer ketika menerima pesan
SIZE = 1024

# membuat objek socket (proses pertama)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# koneksi server (proses kedua)
s.connect(server_address)

print
"1. Hello Server"
print
"2. Selamat Pagi Server"
print
"3. Apa Kabar?"
print
"0. Keluar?"

while 1:
    bilangan = raw_input("Pilih Bilangan : ")
    if not bilangan: break

    # mengirim pesan ke server (proses ketiga)
    s.send(bilangan)

    # menerima pesan dari server
    message = s.recv(SIZE)

    if not bilangan: break
    print
    message

s.close()

