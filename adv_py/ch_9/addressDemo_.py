
# Imports
from address import Address

# Construct two addresses
a = Address(4132, "Place Blvd", "Austin", "Nevada", "12345")
b = Address(1300, "Some Road", "Chicago", "Texas", "99102", "12")

# Print addresses
a.display()
b.display()
# Demonstrate the comesBefore method.
if a.comesBefore(b):
    print('a comes before b')
else:
    print('b comes before a')