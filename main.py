from check import Check
from order import Order
from delivery import Delivery
from end_invoice import End_Invoice

class Process:
    def __init__(self):
        self.lst = []

    def __str__(self):
        return f"{self.lst}"

    def add(self, thing):
        self.lst.append(thing)


logistic_process = Process()
with open("order.txt", "r", encoding="utf-8") as forder:
    for line in forder:
        id, customer_name, address, issue_date, cargo, cargo_quantity, cargo_cost = line.split(';')
        id = int(id)
        cargo_quantity = int(cargo_quantity)
        logistic_process.add(Order(id, customer_name, address, issue_date, cargo, cargo_quantity, cargo_cost))

with open("delivery.txt", "r", encoding="utf-8") as fdelivery:
    for line in fdelivery:
        id, id_order, delivery_date, courier_name, price, order_status = line.split(';')
        id = int(id)
        id_order = int(id_order)
        price = int(price)
        logistic_process.add(Delivery(id, id_order, delivery_date, courier_name, price, order_status))


for thing in logistic_process.lst:
    print(str(thing), end='')