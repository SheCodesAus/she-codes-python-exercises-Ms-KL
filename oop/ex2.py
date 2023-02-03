# Q2) Write a class that represents a rectangle shape and has a method for each of the following:
# 1. Calculating the area.
# 2. Calculating the perimeter.
# 3. Calculating the length of the diagonal.
# 4. Determining whether or not the rectangle is a square.

# https://www.w3schools.com/python/ref_func_round.asp



class Rectangle:
    """
    """
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    
    def area (self):
        area = round(self.width * self.height, 2)
        return f"Area = {area}"
    
    def perimeter (self):
        perimeter = round(2*(self.width + self.height),2)
        return f"Perimeter = {perimeter}"
    
    def diagonal (self):
        diagonal = round(((self.width ** 2)+(self.height ** 2)) ** (1/2),2)
        return f"Diagonal = {diagonal}"
            # step 1: square both numbers
            # width to the power of 2 + height to the power of 2
            # (width x width) + (height x height)
            # Step 2: find the square root of step1
            # square root = step1 to the power of 1/2 ( aka 0.5 )
            # square root = step1 ** (1/2)
            # square root = step1 ** 0.5
    
    def is_square (self):
        # if self.height == self.width:
        #     is_square = "is "
        # else:
        #     is_square = "is not "
        # ALT ---- comprehension
        is_square = "is " if self.height == self.width else "is not "
        return f"This {is_square}a square"


my_rectangle = Rectangle (100, 100)

print(my_rectangle.area())
print(my_rectangle.perimeter())
print((my_rectangle.diagonal()))
print((my_rectangle.is_square()))




# Square a number
    # numb = number to square
        # numb ** 2

# Find square root of number
    # N = squared number
    # n = 
    # N ** (1/2)

# Find the 8th root of a number
    # N ** (1/8)

# print(25 ** (1/2))