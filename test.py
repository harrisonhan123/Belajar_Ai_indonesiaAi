list1 = ['apple','banana','watermelon']
list2 = [2,1,2,7,4,10]
list2.sort()
print(list2)
list3 =list2.reverse()
print(list3)
print(list2.count(2))

print(list1[2])
list1[2]='cerry'
print(list1)

# membership test
print('watermelon' not in list1)

list1.append('avocado')
print(list1)

tuple1 = ('apple','banana','watermelon')
tuple2 = (2,1,2,7,4,10)
print(tuple1[1])

# read file
#data = open('./file_data.txt', mode='r', encoding='utf-8')
#print(data.read())

# append file
#data = open('./file_data.txt', mode='a',encoding='utf-8')
#data.write("\nYuk belajar bahas pemograman Python!")
#data.write("\nasjfda;jsdfajsdfljas;f")
#data.close()

# write file
# data = open('./file_data.txt', mode='w',encoding='utf-8')
# data.write("\n12345677890")
# data.close()

# # better practice
# try:
#     f = open('./file_data.txt',mode='w', encoding='utf-8')
# finally:
#     f.close()

# # best practice
# with open('./file_data.txt',mode='w', encoding='utf-8') as f:
#     # bisa diisi dgn koding 
#     pass

fruit_list = ['apple', 'banana', 'watermelon']

# print(dir(locals()['__builtins__'])) # utk lihat built in function

nilai = 10
pembagi = 0
# try:
#     hasil = nilai/pembagi
# except Exception as e:
#     print("Ooop! terjadi ",e.__class__,'.')

# atau kalau banyak mau di detect errornya
try:
    hasil = nilai/pembagi
except ZeroDivisionError:
    print("Terjadi ZeroDivisionError")
except ValueError:
    print("Terjadi value error")
except:
    print("Ooop! terjadi error tidak diketahui")

class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass

number = 10

# while True:
#     try:
#         i_num = int(input("Masukkan angka: "))

#         if i_num<number:
#             raise ValueTooSmallError
#         if i_num>number:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#         print("Angka yg kamu tebak terlalu kecil, coba lagi!")
#         print()
#     except ValueTooLargeError:
#         print("Angka yg kamu tebak terlalu besar, coba lagi!")
#         print()

# print("Betul!! kamu berhasil menebak dgn tepat.")

import Music.Playlist.play as Play
import Music.Playlist.pause as Pause
import Music.Playlist.load as Load

Play.play("Digimon")
Pause.pause("Naruto")
Load.load("peter pan ")