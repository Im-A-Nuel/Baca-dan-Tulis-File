# data=open('D:\\grup a\\71220913\\soal 1.py')
# isi_file=data.read()
# print(isi_file)
# data.close()
# count=""
# for line in data:
#     count+=line
# print('Line count : \n', count)

# data=open('data.txt')
# baris=1
# for line in data:
#     print(f'{baris}. {line}',end='')
#     baris+=1
# data.close()

# data='data.txt'
# isi_data=open(data,'r')
# for line in isi_data:
#     if line.startswith('S'):
#         print(line, end='')
# isi_data.close()

data='data.txt'
isi_data=open(data,'r')
for line in isi_data:
    if line[0]=='P':
        print(line, end='')
isi_data.close()