# Aplikasi Cashier otomatis

Problem definition:
seorang pemilik supermarket berencana melakukan ekspansi bisnis dengan menggunakan metode pembayaran self-service sehingga customer bisa memasukan item yang dibeli, memasukan item yang dibeli, dan harga item yang dibeli dan fitur yang lain.

setelah mengisi daftar belanja yang diinginkan customer kemudian melakukan proses check out barang, bergantung dengan nilai transaksi yang dilakukan maka jumlah yang dibayarkan akan mendapatkan potongan harga sebagai berikut:

- jika total belanja customer diatas Rp. 200.000 maka akan mendapatkan diskon 5%
- jika total belanja customer diatas Rp. 300.000 maka akan mendapatkan diskon 8%
- jika total belanja customer diatas Rp. 500.000 maka akan mendapatkan diskon 10%

## Alur Program:
---
![image](https://user-images.githubusercontent.com/115323333/205337232-7a0f403c-f664-4680-813b-a003554ea99c.png)

## fitur dan code python:
---
untuk fitur yang ada dalam program kasir tersebut di antara lain:

**add_item** fungsi yang akan memasukan nama item, jumlah item dan harga item ke dalam transaksi yang dilakukan customer barang yang dimasukan akan masuk dalam suatu variabel 
       > """"
        fungsi menambahakan item belanja

        parameter 
        nama_item               : str   nama item yang akan dibeli
        jumlah_item             : int   jumlah item yang akan dibeli
        harga_item              : int   harga item yang akan dibeli
        """

        self.data_kashir.update({nama_item : [jumlah_item, harga_item, jumlah_item *  harga_item]})
        print("selamat anda berhasil menambahkan item belanja !!!")
        
**update_item_name** fungsi yang akan merubah nama item, yang telah dimasukan ke dalam data dengan cara merubah nama item yang ada.

        """"
        fungsi merubah nama item

        parameter 
        nama_item               : str   nama item yang akan dibeli
        nama_item               : str   nama baru item
        """

        temp = self.data_kashir[nama_item]
        self.data_kashir.pop(nama_item)
        self.data_kashir.update({nama_baru : temp})
        print("selamat anda berhasil merubah nama item !!!")
        
**update_jumlah** fungsi yang akan merubah jumlah item dengan mengacu dari nama item, yang telah dimasukan ke dalam data, dengan cara mengisi jumlah item yang baru.
        """"
        fungsi merubah jumlah item

        parameter 
        nama_item               : str   nama item yang akan dibeli
        jumlah_baru             : int   jumlah item yang baru
        """

        self.data_kashir[nama_item][0] = jumlah_baru
        print("selamat anda berhasil merubah jumlah item !!!")
        
**update_harga** fungsi yang akan merubah harga item dengan mengacu dari nama item, yang telah dimasukan ke dalam data. dengan cara mengisi harga item yang baru.
        """"
        fungsi merubah harga item

        parameter 
        nama_item               : str   nama item yang akan dibeli
        harga_baru              : int   harga item yang baru
        """

        self.data_kashir[nama_item][1] = harga_baru
        print("selamat anda berhasil merubah harga item !!!")

**reset_transaction** fungsi yang akan menghapus semua item dalam daftar belanja yang 
        """"
        fungsi menghapus semua item 
        """

        self.data_kashir = {}
        print("anda berhasil menghapus daftar belanja !!!")

**check_order** fungsi yang akan mengecek apakah data yang dimasukan kedalam program sudah sesuai ketentuan yang ada, jika customer menginisiasi item dengan benar maka fungsi akan menampilkan nama item, jumlah item, harga item dan total harga per item.
        """
        fungsi melakukan pengecekan pesanan dan manampilkan daftar belanja
        """

        try:

            for key in self.data_kashir.keys():
                if len(key) > 1:
                    pass
                else:
                    self.update_item_name

            data = pd.DataFrame(self.data_kashir).T
            data.columns = ["Jumlah Item", "Harga Item", "Total harga"]
            print(data.to_markdown())
            print("---"*9)
            print("Pemesanan sudah benar")
            
        except:
            raise TypeError("Anda salah atau belum memasukan nama/jumlah/harga item")
**tabel daftar belanja** 

![image](https://user-images.githubusercontent.com/115323333/205338303-5a628e1b-f61a-4bac-ac03-dbdfb8cc18e0.png)

**total_price** fungsi yang akan melakukan penjumlah semua total harga item dalam daftar belanja, kemudian melakukan branching yang bertujuan potongan harga yang didapatkan customer.
  """"
        fungsi menghitung potongan harga yang didapatkan saat transaksi 
        """
        try:

            total_transaksi = []
            for key, val in self.data_kashir.items():
                total = total_transaksi.append(self.data_kashir[key][2])

            if sum(total_transaksi) > 200_000 & sum(total_transaksi) < 300_000:
                total_belanaja = sum(total_transaksi) * 0.95
                discount = "5%"
                print(f"selamat anda mendapatkan diskon {discount}, sehingga Total belanja anda menjadi Rp.{total_belanaja}")
            elif sum(total_transaksi) > 300_000 & sum(total_transaksi) < 500_000:
                total_belanaja = sum(total_transaksi) * 0.92
                discount = "8%"
                print(f"selamat anda mendapatkan diskon {discount}, sehingga Total belanja anda menjadi Rp.{total_belanaja}")
            elif sum(total_transaksi) > 500_000:
                total_belanaja = sum(total_transaksi) * 0.92
                discount = "8%"
                print(f"selamat anda mendapatkan diskon {discount}, sehingga Total belanja anda menjadi Rp.{total_belanaja}")
            else:
                print(f"Total belanja anda adalah Rp.{sum(total_transaksi)}")

        except:
            raise TypeError("ada yang salah, silahkan gunakan fungsi check_order")

dalam fitur yang ada bila sukses menginisiasi data item maka program akan melakukan printing kalimat yang menjelaskan fungsi yang dilakukan berjalan sukses misal setelah customer melakukan fungsi add_item maka fungsi akan menampilkan pesan “selamat anda berhasil menambahkan item belanja !!!” ini juga berlaku pada setiap fungsi dengan pesan yang menjelaskan proses yang dilakukan.

bila customer telah selesai dalam memasukan item belanja maka proses check order akan melakukan pemeriksaan apakah customer salah memasukan input data sebelumnya, jika customer keliru memasukan data dalam daftar belanja maka check order akan menampilkan tulisan “TypeError("Anda salah atau belum memasukan nama/jumlah/harga item")”. 

setelah melakukan revisi dalam daftar belanja fungsi akan menampilkan tabel daftar belanja customer, setelah itu customer dapat melakukan fungsi total_price untuk mengetahui total harga semua item dalam transaksi yang dilakukan.

## Test Case:
test dilakukan dengan menggunakan file jupyter notebook baru, proses awal dimulai dengan melakukan import file yang akan digunakan, kemudian menginisiasi class dalam file.

![image](https://user-images.githubusercontent.com/115323333/205338555-65351eaf-df9d-465a-b73b-d0021092bf3d.png)

**test 1.** adalah menginput item belanja kedalam fungsi add_item.

![image](https://user-images.githubusercontent.com/115323333/205338587-6fa4c18c-7e33-46dc-ac4f-7876bbe0563d.png)

setelah berhasil menginput item belanja customer, maka fungsi akan menampilkan pesan yang menyatakan item telah masuk dalam daftar belanja customer.

**test 2.** adalah menghapus item dalam list belanja

![image](https://user-images.githubusercontent.com/115323333/205338682-2d88563c-38d3-45e1-a79b-1928d10c854d.png)

customer melakukan penghapus item menggunakan fungsi delete_item dengan menginput nama item yang akan dihapus maka akan menghapus juga data harga, jumlah dan total harga per item dalam daftar belanja.

**test 3.** adalah menghapus semua item dalam daftar belanja

![image](https://user-images.githubusercontent.com/115323333/205338754-a053a784-d027-4168-958b-667cf790280e.png)

customer menghapus semua item dalam daftar belanja sebelumnya, setelah berhasil menghapus semua item dalam daftar maka akan muncul pesan yang menyatakan penghapusan item telah berhasil.

**test 4.** adalah memasukan daftar belanja baru

![image](https://user-images.githubusercontent.com/115323333/205338809-5530b343-697c-4a30-9b4c-d09296029a59.png)

customer memasukan item yang baru dalam daftar belanja yang telah diinisiasi sebelumnya, setelah melakukan pengecekan menggunakan check_order dan tidak terdapat error dalam program maka proses menghitung total biaya yang perlu dibayarkan customer bisa dilakukan.

## Kesimpulan
---
dalam self service cashier ini customer bisa melakukan proses belanja secara mandiri tanpa didampingi oleh petugas pembayaran. dengan menggunakan fungsi add_item, update_item_name, update_jumlah, update_harga, delete_item, reset_transaction, check_order dan total_price.

## Future improvement
---
untuk proses improvement selanjutnya bila diberikan sumber daya yang lebih akan dirangkum dalam list berikut:
1.	membuat database yang berisikan data nama item dan harga yang bisa dirujuk dalam proses transaksi sehingga customer experience akan lebih dimudahkan dalam transaksi menggunakan aplikasi tersebut.
2.	membuat sistem yang akan mencatat transaksi yang dilakukan oleh customer saat berbelanja sehingga masing-masing transaksi akan memiliki unik id tersendiri, dalam unik id tersebut akan terdapat relasi data tanggal transaksi, total transaksi dan kategori item yang dibeli oleh customer.
3.	membuat dashboard penjualan dan transaksi yang telah akan terupdate secara real time dengan transaksi yang dilakukan oleh customer.









