# Q1) Together, we wrote a class for a Book object. 
# Update this class to add the ability to:

# 1. Go directly to a specific page number.

# 2. Bookmark a specific page number, i.e. not just the current page.

# 3. Automatically go back to the start of the book (i.e. page 1) when the user turns the final page.


class Book:
    
    def __init__(self, title, author, pages, current_page, true_or_false, goto, bookmark):
        # initialise arguments title and author
        # these are attributes
        # pass in the title and author
        '''
        insert
        Args:

        Return:
        
        '''
        # initialise
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.true_or_false = true_or_false
        self.goto = goto
        self.bookmark = bookmark
    
    # ---- 

    def bookmark_page(self):
        # self.bookmark = self.current_page
        self.bookmark_page = self.bookmark
    
    # def turn_page(self):
    #     self.current_page += 1
    
    # def back_page(self):
    #     self.current_page -= 1
    
    def turn_page(self):
        if self.true_or_false == True:
            if self.current_page == self.pages:
                self.current_page = 1
            else:
                self.current_page += 1

        else:
            self.current_page -= 1
    
    def go_to(self):
        self.current_page = self.goto

    # ---- class specific overwriting function

    def __str__ (self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__ (self):
        return self.pages

my_book = Book ("A Great Book", "me", 198, 1, True, 197, 22)
# title, author, pages, current_page, true_or_false, goto, bookmark

print(my_book)

# ------ apply function
# my_book.go_to()
# print(my_book.current_page)

# my_book.bookmark_page()
# print(my_book.bookmark_page)

# ------ apply function
# my_book.bookmark_page()
# print(my_book.bookmark)

# ------ apply function
# my_book.turn_page()
# my_book.bookmark_page()
# print(my_book.bookmark)

# ------ apply function
# my_book.back_page()
# my_book.bookmark_page()
# print(my_book.bookmark)

# ------ apply function
print(my_book)
print(my_book.current_page)
my_book.turn_page()
print(my_book.current_page)
my_book.go_to()
print(my_book.current_page)
my_book.turn_page()
print(my_book.current_page)
my_book.turn_page()
print(my_book.current_page)