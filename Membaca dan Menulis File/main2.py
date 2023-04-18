nama_file='transkrip.txt'
handle=open(nama_file,'r')
no_baris=1
print('Daftar Matakuliah yang diambil : ')
total_sks=0
total_bobot=0
sks=0
total_mat=1
harus_diulang=''
for baris in handle:
    if no_baris % 3==1:
        print(f'{total_mat}.{baris}', end='')
        total_mat+=1
        matakuliah=baris.strip()
    if no_baris % 3==2 : #untuk baca sks
        total_sks=total_sks+int(baris)
        sks=int(baris)
    if no_baris % 3 == 0: #untuk baca nilai A/B/C/D/E
        if baris.strip() == 'A':
            total_bobot= total_bobot + sks*4
        elif baris.strip() =='B':
            total_bobot= total_bobot + sks*3
        elif baris.strip() =='C':
            total_bobot= total_bobot + sks*2
        elif baris.strip() =='D':
            total_bobot= total_bobot + sks*1
        elif baris.strip() =='E':
            harus_diulang=harus_diulang+matakuliah+'\n'
            

    no_baris+=1
print(f'Total SKS : {total_sks} SKS')
print(f'IP Semester : {total_bobot/total_sks:.2f}')
print(f'Mata Kuliah yang perlu diulang : {harus_diulang}')
handle.close()