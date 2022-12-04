import pandas as pd

class Kashir:
    def __init__(self):
        """
        fungsi membuat dictionary dan list
        """

        self.data_kashir      = dict() 

    def add_item(self, nama_item, jumlah_item, harga_item):
        """"
        fungsi menambahakan item belanja

        parameter 
        nama_item               : str   nama item yang akan dibeli
        jumlah_item             : int   jumlah item yang akan dibeli
        harga_item              : int   harga item yang akan dibeli
        """

        self.data_kashir.update({nama_item : [jumlah_item, harga_item, jumlah_item * harga_item]})
        print("selamat anda berhasil menambahkan item belanja !!!")

    def update_item_name(self, nama_item, nama_baru):
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

    def update_jumlah(self, nama_item, jumlah_baru):
        """"
        fungsi merubah jumlah item

        parameter 
        nama_item               : str   nama item yang akan dibeli
        jumlah_baru             : int   jumlah item yang baru
        """

        self.data_kashir[nama_item][0] = jumlah_baru
        print("selamat anda berhasil merubah jumlah item !!!")

    def update_harga(self, nama_item, harga_baru):
        """"
        fungsi merubah harga item

        parameter 
        nama_item               : str   nama item yang akan dibeli
        harga_baru              : int   harga item yang baru
        """

        self.data_kashir[nama_item][1] = harga_baru
        print("selamat anda berhasil merubah harga item !!!")

    def check_order(self):
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


    def delete_item(self, nama_item):
        """"
        fungsi menghapus item 

        parameter 
        nama_item               : str   nama item yang akan dibeli
        """

        self.data_kashir.pop(nama_item)
        print(f"{nama_item} berhasil dihapus dalam daftar belanja anda !!!")

    def reset_transaction(self):
        """"
        fungsi menghapus semua item 
        """

        self.data_kashir = {}
        print("anda berhasil menghapus daftar belanja !!!")

    def total_price(self):
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
                total_belanaja = sum(total_transaksi) * 0.90
                discount = "10%"
                print(f"selamat anda mendapatkan diskon {discount}, sehingga Total belanja anda menjadi Rp.{total_belanaja}")
            else:
                print(f"Total belanja anda adalah Rp.{sum(total_transaksi)}")

        except:
            raise TypeError("ada yang salah, silahkan gunakan fungsi check_order")
