class Address:
    def __init__(self, houseNumber, street, city, state, postalCode, aptNumber=""):
        self.houseNumber = houseNumber
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.aptNumber = aptNumber

    def print(self):
        print('Street: ' + self.street)
        print('City: ' + self.city + ', State: ' + self.state + ', Postal code: ' + self.postalCode)

    def comesBefore(self, other):
        return self.postalCode < other.postalCode