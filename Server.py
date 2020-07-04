#!/usr/bin/env python
# impor modul socket
import socket

# menentukan alamat server
server_address = ('localhost', 4999)

# ukuran buffer ketika menerima pesan
SIZE = 1024

# membuat objek socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ke alamat server
s.bind(server_address)

# mendengarkan koneksi dari client
s.listen(5)

# siap menerima pesan terus-menerus dari client
while 1:
    print
    "Waiting for connection"

    # menerima koneksi dari client
    client, client_address = s.accept()

    print
    "Connected from : ", client_address

    while 1:
    # menerima pesan dari client
    message = client.recv(SIZE)
    if (message == "1"):
        balik = "Hello juga"
    elif (message == "2"):
        balik = "Selamat pagi juga"
    elif (message == "3"):
    balik = "Baik-baik saja"
    else:
    balik = "Tidak ada apa-apa"

    # jika tidak ada pesan, keluar dari while
    if not message: break
    print
    message

