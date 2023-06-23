# Counter controlled loop
## Must have three things, must initialize the counter variable
## Must compare variable to some value
## Must increment or decrement the counter controlled variable

#x = 0
#while x <= 67 :
#   x = x+1
#   print("hello",x)
#
   
# Sentinel controlled loop
#grade = float(input("Enter grade or -1 to end: "))
#total = 0
#while grade > -1:
#   total = total + grade
#   grade = float(input("Enter grade or -1 to end: "))
#print(total)

# Flag controlled loop
flag = True
x=0
while flag:
   print("Hello")
   x = x + 1
   if (x > 5):
      flag = False
