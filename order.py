class Order:
    def __init__(self, id, customer_name, address, issue_date, cargo, cargo_quantity, cargo_cost):
        self.id = id
        self.customer_name = customer_name
        self.address = address
        self.issue_date = issue_date
        self.cargo = cargo
        self.cargo_quantity = cargo_quantity
        self.cargo_cost = cargo_cost

    def __str__(self):
        return f"{self.id} {self.customer_name} {self.address} {self.issue_date} {self.cargo} {self.cargo_quantity} {self.cargo_cost}"
