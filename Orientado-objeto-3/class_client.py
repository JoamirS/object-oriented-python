class Client:
    def __init__(self, name, age):
        self.name = name
        self.name = age
        self.address = []

    def insert_address(self, city, estate):
        self.address.append(Address(city, estate))

    def list_address(self):
        for address in self.address:
            print(address.city, address.estate)


class Address:
    def __init__(self, city, estate):
        self.city = city
        self.estate = estate
