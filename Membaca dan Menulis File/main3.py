nama_file='buah.txt'
handle=open(nama_file,'a')

nama_buah=input('Masukan nama buah : ')
handle.write(nama_buah +'\n')

handle.close()