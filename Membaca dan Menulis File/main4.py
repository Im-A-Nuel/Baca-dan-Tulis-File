buah_sekarang=input('Buah mana yang mau diganti : ')
buah_baru=input('Mau diganti apa : ')

nama_file='buah.txt'
handle=open(nama_file,'r') #load dulu ke memory

#per baris
isi_file=''
for baris in handle :
    if baris.strip()==buah_sekarang:
        isi_file=isi_file + buah_baru + '\n'
    else :
        isi_file=isi_file + baris

#sudah selesai baca
handle.close()

# ganti ke mode write
handle=open(nama_file,'w')
handle.write(isi_file)
handle.close()