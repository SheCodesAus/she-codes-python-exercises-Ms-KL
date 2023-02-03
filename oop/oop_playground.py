# class Book:
    
#     def __init__(self, title, author, pages, current_page, true_or_false):
#         # initialise arguments title and author
#         # these are attributes
#         # pass in the title and author
#         '''
#         insert
#         Args:

#         Return:
        
#         '''
#         # initialise
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
#         self.bookmark = 1
#         self.true_or_false = true_or_false
    
#     # ---- 

#     def bookmark_page(self):
#         self.bookmark = self.current_page
    
#     # def turn_page(self):
#     #     self.current_page += 1
    
#     # def back_page(self):
#     #     self.current_page -= 1
    
#     def turn_page(self):
#         if self.true_or_false == True:
#             self.current_page += 1
#         else:
#             self.current_page -= 1

#     # ---- class specific overwriting function

#     def __str__ (self):
#         return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

#     def __len__ (self):
#         return self.pages

# my_book = Book ("A Great Book", "me", 198,1, False)
# print(my_book)

# my_book.bookmark_page()
# print(my_book.bookmark)

# my_book.turn_page()
# my_book.bookmark_page()
# print(my_book.bookmark)

# # my_book.back_page()
# # my_book.bookmark_page()
# # print(my_book.bookmark)



# -----------------------------------------------
class Employee:

    # INITIALISE
    def __init__(self, name, salary, start_date, phone_number):
        self.name = name
        self.salary = salary
        self.start_date = start_date
        self.phone_number = phone_number

    # METHODS
    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)
    
    def get_contact_details(self):
        return(self.name, self.phone_number)
    
    # FUNCTIONS (class specific)
    # inset


# CREATE OBJECTS (instance of the class)
employee_1 = Employee("Fran", 7800, "12345678", "1st June 2008")
employee_2 = Employee("Ben", 200000, "9492058", "4th June 2010")

print(employee_1.get_employment_details())
print(employee_2.get_contact_details())
    