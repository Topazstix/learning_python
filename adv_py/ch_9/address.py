## Address class
# Attributes house number, street, city, state, postal code and optional apartment number
class Address : 
    def __init__(self, houseNum, street, city, state, zipCode, aptNum="") :
        self.houseNum = houseNum
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.aptNum = aptNum

    # Method for displaying the information in a human readable format 
    def display(self) :
        if len(self.aptNum) == 0  :
            line1 = "Street: " + str(self.houseNum) + " " + str(self.street)
        else :
            line1 = "Street: " + str(self.houseNum) + " " + str(self.street) + ", Apt Number: " + str(self.aptNum)
        line2 = "\nCity: " + str(self.city) + ", State: " + str(self.state) + ", Zip Code: " + str(self.zipCode)
        print(line1,line2)
        
    # Method tells whether address comes before another according to its zip code
    def comesBefore(self, other) : 
        return self.zipCode < other.zipCode
    
