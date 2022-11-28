"""
GITHUB : galihap76

AUTHOR : Galih Anggoro Prasetya

REPO : https://github.com/galihap76/kuliah/tree/main/semester1/algoritma-dan-pemrograman-1
"""

# import module
import requests, sys
from json import loads

# class Hitung nilai
class Hitung_nilai:

  # init paramater
    def __init__(self, tambah, kurang, kali, bagi):
        self.tambah = tambah
        self.kurang = kurang
        self.kali = kali
        self.bagi = bagi   

  # function nilai tambah
    def nilaiTambah(self):

      # lakukan hitung tambah
        hitungTambah = self.tambah + self.tambah

      # kembalikan nilai hasil tambah
        return hitungTambah

  # function nilai kurang
    def nilaiKurang(self):

      # lakukan hitung kurang
        hitungKurang = self.kurang - 5

      # kembalikan nilai hasil kurang
        return hitungKurang

  # function nilai kali 
    def nilaiKali(self):

      # lakukan hitung kali
        hitungKali = self.kali * self.kali

      # kembalikan nilai hasil kali
        return hitungKali

  # function nilai bagi
    def nilaiBagi(self):

      # lakukan hitung bagi
        hitungBagi = int(self.bagi / self.bagi)

      # kembalikan nilai hasil bagi
        return hitungBagi


  # function main untuk menampilkan hasil program
    def Main(self):
        print(f'Hasil nilai tambah : {self.nilaiTambah()}')
        print(f'Hasil nilai kurang : {self.nilaiKurang()}')
        print(f'Hasil nilai kali : {self.nilaiKali()}')
        print(f'Hasil nilai bagi : {self.nilaiBagi()}')
        print('\n')

# class Author untuk menampilkan data author
class Author:

  # function author
    def author(self):

      # init url author
          META_URL = 'https://raw.githubusercontent.com/galihap76/kuliah/main/semester1/algoritma-dan-pemrograman-1/metadata.json'

      # get data dari variabel META URL
          req_meta = requests.get(META_URL, timeout=5)

      # cek jika status HTTP nya itu 200 berarti itu OK
          if req_meta.status_code == 200:

            # lakukan untuk mengambil data author
              metadata = req_meta.text
              json_data = loads(metadata)
              nama_author = json_data['author']
              nim_author = json_data['nim']
              jurusan_author = json_data['jurusan']

            # cek jika bukan author nya itu Galih Anggoro Prasetya atau NIM nya bukan 22205018
              if 'Galih Anggoro Prasetya' != nama_author or 22205018 != nim_author:

                # beri pesan kesalahan
                  print('[-] Oops ada sesuatu yang tidak valid')

                # dan hentikan program
                  sys.exit()

            # tampilkan data author ketika bernama Galih Anggoro Prasetya dan NIM 22205018
              else:
                  print(40*"=")
                  print(f"""Nama author : {nama_author}
Nim : {nim_author}
Jurusan : {jurusan_author}""")
                  print(40*"=")
                  print('\n')
  
# jalankan program
if __name__ == "__main__":

  # lakukan instance Hitung_nilai dan Author class
    try:
      
      objek1 = Author().author() # objek 1 untuk menampilkan data author
      objek2 = Hitung_nilai(10, 10, 10, 10).Main()  # objek 2 untuk memberikan nilai 10
      objek3 = Hitung_nilai(20, 20, 20, 20).Main()  # objek 3 untuk memberikan nilai 20
      objek4 = Hitung_nilai(30, 30, 30, 30).Main()  # objek 4 untuk memberikan nilai 30
      objek5 = Hitung_nilai(40, 40, 40, 40).Main()  # objek 5 untuk memberikan nilai 40
      objek6 = Hitung_nilai(50, 50, 50, 50).Main()  # objek 6 untuk memberikan nilai 50

    # error handling ketika koneksi error   
    except requests.exceptions.ConnectionError:
        print('[-] Oops koneksi error')
        sys.exit()
