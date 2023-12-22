class End_Invoice:
    def __init__(self, id, customers_name, address, issue_date, cargo, cargo_quantity, cost, order_status):
        self.id = id
        self.customers_name = customers_name
        self.address = address
        self.issue_date = issue_date
        self.cargo = cargo
        self.cargo_quantity = cargo_quantity
        self.cost = cost
        self.order_status = order_status