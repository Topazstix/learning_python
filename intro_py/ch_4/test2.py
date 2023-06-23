# def main() :
#     n = int(input("Please enter the upper limit: "))
#     if n >= 2 :
#       print(2)
#     i = 3
#     while i <= n :
#       if isprime(i) :
#          print(i)
#       i = i + 2
  
# #  Tests whether an integer is a prime.
# #  @param n any positive integer
# #  @return True if n is a prime, False otherwise
# def isprime(n) :
#    if n == 1 :
#       return False
  
#    if n == 2 : 
#       # 2 is a prime 
#       return True 
  
#    if n % 2 == 0 : 
#       # No other even number is a prime 
#       return False 
  
#    # Try finding a number that divides n 
#    k = 3 # No need to divide by 2 because n is odd 
#    # Only need to try divisors up to sqrt(n) 
#    while k * k <= n : 
#       if n % k == 0 : 
#          # n is not a prime because it is divisible by k 
#          return False 
#       # Try next odd number 
#       k = k + 2 
  
#    # No divisor found. Therefore, n is a prime 
#    return True 
  
# # Start the program.
# main()

# def get_float():
#    while True:
#       try:
#          return float(input ("Enter your second number: "))
#       except ValueError:
#          print("When I ask for a number, give me a number. Come on!")

# def get_two_floats():
#    return get_float(), get_float()


# def get_two_floats():
#     while True:
#         try:
#             n1 = float(input ("Enter your first number: "))
#             n2 = float(input ("Enter your second number: "))
#             n1 = "%.3f" %n1
#             n2 = "%.3f" %n2
#         except ValueError:
#             print("When I ask for a number, give me a number. Come on!")
#         else:
#             return n1, n2
# get_two_floats()



def test_validation():
   flag = False
   while not flag:
      try:
         radius=float(input("Enter radius of cone: "))
         height=float(input("Enter height of cone: "))
         radius = float("%.3f" %radius)
         height = float("%.3f" %height)
         flag = True
         return radius, height
         # coneVolume(radius, height)
         # coneSurface(radius, height)

      except ValueError:
         print("Enter correct number format")

        # radius = float(input("Enter radius of cone: "))
        # height = float(input("Enter height of cone: "))
        # radius = float("%.3f" % radius)
        # height = float("%.3f" % height)
        # coneVolume(radius, height)
        # coneSurface(radius, height)

               
test_validation()


      #   flag = False
      #   while not flag:
      #       try:
      #           radius=float(input("Enter radius of cone: "))
      #           height=float(input("Enter height of cone: "))
      #           radius = "%.3f" %radius
      #           height = "%.3f" %height
      #           flag = True
      #           coneVolume(radius, height)
      #           coneSurface(radius, height)

      #       except ValueError:
      #           print("Enter correct number format")
   

# ##
# #  This program grades a multiple choice exam in which each question has four
# #  possible choices: a, b, c, or d.
# #

# # Define a string containing the correct answers.
# CORRECT_ANSWERS = "adbdcacbdac"

# # Obtain the user's answers, and make sure enough answers are provided.
# done = False
# while not done :
#    userAnswers = input("Enter your exam answers: ")
#    if len(userAnswers) == len(CORRECT_ANSWERS) :
#       done = True     
#    else :
#       print("Error: an incorrect number of answers given.")    
        
# # Check the exam.
# numQuestions = len(CORRECT_ANSWERS)
# numCorrect = 0
# results = ""

# for i in range(numQuestions) :
#    if userAnswers[i] == CORRECT_ANSWERS[i] :
#       numCorrect = numCorrect + 1
#       results = results + userAnswers[i]
#    else :
#       results = results + "X"
      
# # Grade the exam.
# score = round(numCorrect / numQuestions * 100)

# if score == 100 :
#    print("Very Good!")
# else :
#    print("You missed %d questions: %s" % (numQuestions - numCorrect, results))
   
# print("Your score is: %d percent" % score)   

from math import pi,sqrt


def Area_of_Triangle(radius):
    sa =  4 * pi * radius * radius
    Volume = (4 / 3) * pi * radius * radius * radius
    print("\n The Surface area of a Sphere = %.2f" %sa)
    print("\n The Volume of a Sphere = %.2f" %Volume)

def Vol_Sa_Cylinder(radius, height):
    sa = 2 * pi * radius * (radius + height)
    Volume = pi * radius * radius * height
    L = 2 * pi * radius * height
    T = pi * radius * radius

    print("\n The Surface area of a Cylinder = %.2f" %sa)
    print(" The Volume of a Cylinder = %.2f" %Volume)
    print(" Lateral Surface Area of a Cylinder = %.2f" %L)
    print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)
