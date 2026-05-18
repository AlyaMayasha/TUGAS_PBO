# Program ini melanggar prinsip SOLID karena banyak class memiliki tanggung jawab yang tidak sesuai dan saling bergantung langsung

class FoodOrderSystem:
    # SRP dilanggar: satu class memiliki banyak tugas
    def order_food(self):
        print("Memesan makanan")
    def print_receipt(self):
        print("Mencetak struk")
    def send_notification(self):
        print("Mengirim notifikasi")
    def save_order(self):
        print("Menyimpan pesanan")

class PaymentService:
    # OCP dilanggar: jika ada metode pembayaran baru maka method harus diubah
    def pay(self, method):
        if method == "cash":
            print("Pembayaran Tunai")
        elif method == "qris":
            print("Pembayaran QRIS")

class Delivery:
    def deliver(self):
        print("Pesanan dikirim")

class Pickup(Delivery):
    # LSP dilanggar: subclass tidak bisa menggantikan parent
    def deliver(self):
        raise Exception(
            "Pickup tidak perlu pengiriman"
        )

class RestaurantEmployee:
    def take_order(self):
        pass
    def manage_kitchen(self):
        pass
    def make_financial_report(self):
        pass

class Cashier(RestaurantEmployee):
    def take_order(self):
        print("Kasir menerima pesanan")
    # ISP dilanggar: kasir dipaksa memakai method yang tidak dibutuhkan
    def manage_kitchen(self):
        raise Exception(
            "Kasir tidak mengelola dapur"
        )
    def make_financial_report(self):
        raise Exception(
            "Kasir tidak membuat laporan"
        )

class CashPayment:
    def pay(self, amount):
        print(
            f"Pembayaran Tunai : Rp {amount}"
        )

class OrderService:
    # DIP dilanggar: bergantung langsung pada class konkret
    def __init__(self):
        self.payment = CashPayment()
    def checkout(self):
        self.payment.pay(25000)

# ====================
# MAIN PROGRAM
# ====================

system = FoodOrderSystem()

system.order_food()
system.print_receipt()
system.send_notification()
system.save_order()

payment = PaymentService()
payment.pay("qris")
order = Pickup()
try:
    order.deliver()
except Exception as e:
    print(e)

cashier = Cashier()
cashier.take_order()
service = OrderService()
service.checkout()