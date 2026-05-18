Tugas Pemrograman Berbasis Objek / OOP
Materi SOLID
Anggota Kelompok :
Alya Mayasha | 2409106054
Nou Julyanah Mazuwa | 2409106066
Keysha Khoirunnisa Aulia Khotim | 2409106077
Aulia Natasya | 2409106084

🍔 SOLID Principles — Sistem Pemesanan Makanan

README ini menjelaskan penerapan lima prinsip SOLID menggunakan contoh sederhana sistem pemesanan makanan dengan bahasa Python.

Daftar Isi
SRP — Single Responsibility Principle
OCP — Open/Closed Principle
LSP — Liskov Substitution Principle
ISP — Interface Segregation Principle
DIP — Dependency Inversion Principle

**SRP — Single Responsibility Principle**
"Sebuah class hanya boleh memiliki satu tanggung jawab."

❌ Anti-Pattern
class FoodOrderSystem:
    def order_food(self):
        pass
    def print_receipt(self):
        pass
    def send_notification(self):
        pass
    def save_order(self):
        pass

Masalah
Satu class menangani terlalu banyak tugas seperti pemesanan makanan, mencetak struk, mengirim notifikasi, dan menyimpan data pesanan.

✅ Pattern yang Benar
class Food:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name

class OrderService:
    def order_food(self,food):
        print("Memesan makanan: "+food.get_name())

class ReceiptService:
    def print_receipt(self,food):
        print("Struk pesanan: "+food.get_name())

food=Food("Nasi Goreng")
order=OrderService()
receipt=ReceiptService()
order.order_food(food)
receipt.print_receipt(food)

Keuntungan
Setiap class hanya fokus pada satu tugas sehingga program lebih mudah dipahami dan dikembangkan.

**OCP — Open/Closed Principle**
"Class terbuka untuk pengembangan, tetapi tertutup untuk modifikasi."

❌ Anti-Pattern
class PaymentService:
    def pay(self,method):
        if method=="cash":
            print("Pembayaran Tunai")
        elif method=="qris":
            print("Pembayaran QRIS")

Masalah
Jika ingin menambahkan metode pembayaran baru, maka kode lama harus diubah.

✅ Pattern yang Benar
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CashPayment(Payment):
    def pay(self,amount):
        print("Pembayaran Tunai : Rp "+str(amount))

class QRISPayment(Payment):
    def pay(self,amount):
        print("Pembayaran QRIS : Rp "+str(amount))

payment=QRISPayment()
payment.pay(25000)

Keuntungan
Menambah metode pembayaran baru cukup membuat class baru tanpa mengubah kode lama.

**LSP — Liskov Substitution Principle**
"Subclass harus dapat menggantikan superclass tanpa merusak program."

❌ Anti-Pattern
class Delivery:
    def deliver(self):
        print("Pesanan dikirim")

class Pickup(Delivery):
    def deliver(self):
        raise Exception(
            "Pickup tidak perlu pengiriman"
        )

Masalah
Class Pickup tidak bisa menggantikan Delivery dengan baik karena menyebabkan error.

✅ Pattern yang Benar
from abc import ABC,abstractmethod
class OrderType(ABC):
    @abstractmethod
    def process(self):
        pass

class DeliveryOrder(OrderType):
    def process(self):
        print("Pesanan dikirim ke alamat")

class PickupOrder(OrderType):
    def process(self):
        print("Pesanan diambil langsung")

order1=DeliveryOrder()
order2=PickupOrder()
order1.process()
order2.process()

Keuntungan
Semua subclass dapat digunakan tanpa menyebabkan error pada program.

**ISP — Interface Segregation Principle**
"Class tidak boleh dipaksa menggunakan method yang tidak dibutuhkan."

❌ Anti-Pattern
class RestaurantEmployee:
    def cook_food(self):
        pass
    def take_order(self):
        pass
    def make_report(self):
        pass

class Cashier(RestaurantEmployee):
    def cook_food(self):
        raise Exception(
            "Kasir tidak memasak"
        )
    def take_order(self):
        print("Kasir menerima pesanan")
    def make_report(self):
        raise Exception(
            "Kasir tidak membuat laporan"
        )

Masalah
Class Cashier dipaksa menggunakan method yang tidak dibutuhkan.

✅ Pattern yang Benar
from abc import ABC,abstractmethod
class OrderFeature(ABC):
    @abstractmethod
    def take_order(self):
        pass

class CookFeature(ABC):
    @abstractmethod
    def cook_food(self):
        pass

class Cashier(OrderFeature):
    def take_order(self):
        print("Kasir menerima pesanan")

class Chef(CookFeature):
    def cook_food(self):
        print("Chef memasak makanan")

cashier=Cashier()
chef=Chef()
cashier.take_order()
chef.cook_food()

Keuntungan
Setiap class hanya menggunakan interface yang sesuai dengan kebutuhannya.

**DIP — Dependency Inversion Principle**
"Class tingkat tinggi tidak boleh bergantung pada class konkret, tetapi pada abstraksi."

❌ Anti-Pattern
class CashPayment:
    def pay(self,amount):
        print(
            "Pembayaran Tunai : Rp "
            +str(amount)
        )

class OrderService:
    def __init__(self):
        self.payment=CashPayment()
    def checkout(self):
        self.payment.pay(25000)

Masalah
OrderService bergantung langsung pada CashPayment.

✅ Pattern yang Benar
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CashPayment(Payment):
    def pay(self,amount):
        print(
            "Pembayaran Tunai : Rp "
            +str(amount)
        )

class QRISPayment(Payment):
    def pay(self,amount):
        print(
            "Pembayaran QRIS : Rp "
            +str(amount)
        )

class OrderService:
    def __init__(self,payment):
        self.payment=payment
    def checkout(self,amount):
        self.payment.pay(amount)

payment=QRISPayment()
order=OrderService(payment)
order.checkout(25000)

Keuntungan
Program menjadi fleksibel karena tidak bergantung pada class tertentu.