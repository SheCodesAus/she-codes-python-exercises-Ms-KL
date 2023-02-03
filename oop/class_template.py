

# ----- CLASS -----
class Class_name_w_capital():
    '''
    This is the docstring explanation of what the class does
    '''
    # CLASS VARIABLES -----
    count = 0
    school_name = "She Codes"

    # CONSTRUCTOR -----
    def __init__(self, firstname, lastname, id):
        # OBJECT VARIABLES / ATTRIBUTES -----
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        Class_name_w_capital.count +=1

    # METHODS / ACTIONS on OBJECTS -----
    def full_name(self):
        '''
        Method:     Creates a full name using the firstname and lastname
        Invoke:     object1 = Class_name_w_capital(firstname, lastname, id)
                    print(object1.full_name())
        returns:    the first and last name as a string
        eg:         first_name last_name
        '''
        return f"{self.firstname} {self.lastname}"
    
    def email(self, domain_name):
        ''' 
        Method:     Creates a student email address using the id and domain name
        pass in:    domain name as a string
        eg:         object1 = Class_name_w_capital(firstname, lastname, id)
                    print(object1.email("domain_name"))
        returns:    the id number and domain name as a string
        eg:         id@domain_name
        '''
        return f"{self.id}@{domain_name}"

    # METHODS / ACTIONS on CLASS VARIABLES -----
    @classmethod
    def change_school_name (cls, new_school_name):
        '''
        Method:     Changes the Class Variable school_name using the new_school_name
        Pass in:    new school name as a string
        eg:         Class_name_w_capital.school_name("new_school_name")
                    print(Class_name_w_capital.school_name)
        Returns:    The new school name as a string
        '''
        Class_name_w_capital.school_name = new_school_name
        
    # STATIC METHODS / ACTIONS NOT on objects/class -----
    @staticmethod
    def greeting():
        '''
        Method:     Uses the class variable to return a greeting to the class and any object within the class
        Invoke:     print(class_name_w_capital.greeting())
                    print(obj1.greeting())
        Return:     Welcome to <school_name>!"
                    Welcome to <school_name>!"
        '''
        return f"Welcome to {Class_name_w_capital.school_name}!"
    
    # SPECIAL METHODS / ACTIONS on existing __dunder__ methods
    def __str__ (self):
        '''
        Current:    returns--> __main__.Class_name_w_capital object at <pclocation>
        Override:   Overrides the __str__ method to return the objects's firstname, lastname and id number
        eg:         object1 = Class_name_w_capital("firstname", "lastname" , id)
                    print(object1)
        Returns:    objects's firstname, lastname and id number as a string
        eg:         firstname lastname's, id number is id
        '''
        return f"{self.firstname} {self.lastname}'s, id number is {self.id}"


# ----- INSTANTIATE OBJECTS -----

student1 = Class_name_w_capital("John", "Smith", 1)
student2 = Class_name_w_capital("Sally", "Brown", 2)

# ----- INVOKE & RETURN-----
print("       ")
print(f"print(student1) = {student1}")
print(f"print(student2) = {student2}")
print("       ")
print(f"print(Class_name_w_capital.school_name) = {Class_name_w_capital.school_name}")
print(f"Change the school name by invoking: Class_name_w_capital.change_school_name('She Codes Australia')")
Class_name_w_capital.change_school_name("She Codes Australia")
print(f"print(Class_name_w_capital.school_name) = {Class_name_w_capital.school_name}")
print("       ")
print(f"print(Class_name_w_capital.greeting()) = {Class_name_w_capital.greeting()}")
print("       ")
print(f"print(student1.greeting()) = {student1.greeting()}")

# ------- CHILD / SUBCLASS --------

class Child_subclass(Class_name_w_capital):
    '''
    Parent:         Class_name_w_capital. Child_subclass inherits all parent attributes
    Child:          Added language attribute and argument.
                    __str__ updated
    '''
    
    # CONSTRUCTOR -----
    def __init__(self, firstname, lastname, id, language):
        # OBJECT VARIABLES / ATTRIBUTES -----
        super().__init__(firstname, lastname, id)
        self.language = language

    # SPECIAL METHODS / ACTIONS on existing __dunder__ methods
    def __str__(self):
        '''
        Current:    returns--> inherited --> firstname lastname's, id number is id
        Override:   Overrides the parent __str__ method to 
                    return the objects's firstname, lastname, id number and language as a string
        eg:         object2 = Child_subclass("firstname", "lastname" , id, "Python")
                    print(object2)
        Returns:    objects's firstname, lastname, id number and language as a string
        eg:         firstname lastname's, id number is id, student knows Python programming
        '''
        return f"{self.firstname} {self.lastname}'s id number is {self.id}, student knows {self.language} programming"

# ----- INSTANTIATE OBJECTS -----

student3 = Child_subclass("Fred", "Flinstone", 3, "Python")
student4 = Child_subclass("Bonnie", "Doone", 4, "C++")

# ----- INVOKE & RETURN-----
print("       ")
print(f"print(student1) = {student1}")
print(f"print(student2) = {student2}")
print(f"print(student3) = {student3}")
print(f"print(student4) = {student4}")
print("       ")
print(student1.email("yahoo.com"))
print(student4.email("hotmail.com"))
print("       ")
print(f"Student4 is object of Parent class? {isinstance(student4, Class_name_w_capital)}")
print(f"Student4 is object of Child class? {isinstance(student4, Child_subclass)}")
print(f"Student1 is object of Parent class? {isinstance(student1, Class_name_w_capital)}")
print(f"Student1 is object of Child class? {isinstance(student1, Child_subclass)}")
print("       ")
print(f"Parent is subclass of child? {issubclass(Class_name_w_capital, Child_subclass)}")
print(f"Child is subclass of parent? {issubclass(Child_subclass, Class_name_w_capital)}")
print("       ")
print(f"Student1 has attribute: language? {hasattr(student1,'language')}")
print(f"Student4 has attribute: language? {hasattr(student4,'language')}")
print("       ")
print(dir(Class_name_w_capital))
print("       ")
print(dir(Child_subclass))
print("       ")
print(help(Class_name_w_capital))
print("       ")
print(help(Child_subclass))
print("       ")
print(Class_name_w_capital.__doc__)
print("       ")
print(Class_name_w_capital.__dict__)