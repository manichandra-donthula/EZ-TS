#create a class that consists of three variables with iniatialization and you have to take two methods and first method is 
#two argumented function frst one string type of argument and second one is int type if argument and inside of the method 
#reverse of string should be printed and square root of integer argument value also. The second method is displayResults one statement 
#should print length of string and another statement should print modulus division of two integer variables.

class problem_1:
    def __init__(self, str1, int1, int2):
        self.str1 = str1
        self.int1 = int1
        self.int2 = int2
    def method_1(self, str1, int1):
        print("\nReverse of given string is: ", str1[::-1])
        print("Square root of int: ", int1**0.5)
    def displayResults(self):
        print("Length of the given string is: ", len(self.str1))
        print("The modulus division of two integers: ", self.int1%self.int2)

str1 = str(input("Enter a string value: "))
int1 = int(input("Enter an integer value: "))
int2 = int(input("Enter another integer value: "))
obj1 = problem_1(str1, int1, int2)
obj1.method_1(str1, int1)
obj1.displayResults()