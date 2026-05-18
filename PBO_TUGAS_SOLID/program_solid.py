# Program ini menerapkan prinsip SOLID

from abc import ABC, abstractmethod

# ====================
# SRP
# ====================

# Class hanya fokus memesan makanan
class OrderService:
    def order_food(self):
        print("Memesan makanan")

# Class hanya fokus mencetak struk
class ReceiptService:
    def print_receipt(self):
        print("Mencetak struk")

# Class hanya fokus notifikasi
class NotificationService:
    def send_notification(self):
        print("Mengirim notifikasi")

# ====================
# OCP + DIP
# ====================

# Interface pembayaran
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Implementasi pembayaran tunai
class CashPayment(Payment):
    def pay(self, amount):
        print(
            f"Pembayaran Tunai : Rp {amount}"
        )

# Implementasi pembayaran QRIS
class QRISPayment(Payment):
    def pay(self, amount):
        print(
            f"Pembayaran QRIS : Rp {amount}"
        )

# ====================
# LSP
# ====================

# Semua jenis pesanan dapat diproses dengan aman
class OrderType(ABC):
    @abstractmethod
    def process(self):
        pass

class DeliveryOrder(OrderType):
    def process(self):
        print(
            "Pesanan dikirim ke alamat"
        )

class PickupOrder(OrderType):
    def process(self):
        print(
            "Pesanan diambil langsung"
        )

# ====================
# ISP
# ====================

# Interface dipisah sesuai kebutuhan
class OrderFeature(ABC):
    @abstractmethod
    def take_order(self):
        pass

class KitchenFeature(ABC):
    @abstractmethod
    def manage_kitchen(self):
        pass

class ReportFeature(ABC):
    @abstractmethod
    def make_financial_report(self):
        pass

class Cashier(OrderFeature):
    def take_order(self):
        print(
            "Kasir menerima pesanan"
        )

class Chef(KitchenFeature):
    def manage_kitchen(self):
        print(
            "Chef mengelola dapur"
        )

class Manager(ReportFeature):
    def make_financial_report(self):
        print(
            "Manager membuat laporan"
        )

# ====================
# DIP
# ====================

# Bergantung pada abstraksi, bukan class konkret
class CheckoutService:
    def __init__(self, payment):
        self.payment = payment
    def checkout(self, amount):
        self.payment.pay(amount)

# ====================
# MAIN PROGRAM
# ====================

# SRP
order = OrderService()
receipt = ReceiptService()
notification = NotificationService()

order.order_food()
receipt.print_receipt()
notification.send_notification()

# OCP + DIP
payment = QRISPayment()
checkout = CheckoutService(payment)
checkout.checkout(25000)

# LSP
order1 = DeliveryOrder()
order2 = PickupOrder()

order1.process()
order2.process()

# ISP
cashier = Cashier()
chef = Chef()
manager = Manager()

cashier.take_order()
chef.manage_kitchen()
manager.make_financial_report()