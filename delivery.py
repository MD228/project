class Delivery:
    def __init__(self, id, id_order, delivery_date, courier_name, price, order_status):
        self.id = id
        self.id_order = id_order
        self.delivery_date = delivery_date
        self.courier_name = courier_name
        self.price = price
        self.order_status = order_status


    def __str__(self):
        return f"{self.id} {self.id_order} {self.delivery_date} {self.courier_name} {self.price} {self.order_status}"