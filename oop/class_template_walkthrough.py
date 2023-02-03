
# -------- COMPLETE CLASS -------- 
    # Class -----
    # eg:               class Class_name:
    # eg output:        print(Class_name)

        # docstring -----
        # EG:           ''' Docstring '''
        # eg output:    print(Class_name.__doc__)   

        # variables -----
        # ?? change these values using @classmethod
        # EG:           x = 0
        # EG Output:    print(Class_name.x)
        # EG:           name = "class-a-thon"


        # constructor -----
        # ?? instantiates objects inside class
        # EG:           def __init__(self, arg1, arg2 etc)
        # EG Output:    print(obj1.arg1)

            # attributes -----
            # ?? self refers to objects, name & number of args and attributes should match
            # EG:       self.attr1 = arg1

        # methods -----
        # ?? funcs that allow performing actions in class OR specify behaviour of objects
            # EG:
                        # def func_name(self,<args>):
                            # action block
                            # return results
            # eg output:    print(obj1.func_name(args))
        
        # CLASS methods -----
        # eg:           @classmethod
                        # def class_method(cls, arg1):
                            # Class_name.x = arg1
                            # this replaces the value @ x in class variables
        # eg output:    print(Class_name.class_method(3))
                        # print(Class_name.x)
        
        # STATIC methods -----
        # ?? no cls or self. Uses variables.
        # eg:           @staticmethod
                        #def static_method():
                            #return f"Welcome to {Class_name.name}!"
        # eg output:    print(Class_name.static_method())
                        #print(obj1.static_method())
        
        # SPECIAL methods -----
        # ?? Magic Overrides built in dunders (__str__, __add__ etc)
        # eg:           def __str__(self):
                            #return f"{self.arg1} {self.arg2}"
        # eg output:    print(obj1)

    # Instantiate -----
    # EG:               obj1 = Complete_class("this is OBJ1's arg1", "this is OBJ1's arg2")

    # Invoke Methods for Output -----
    # EG:               obj1.func_name(<args>)

    # OUTPUT
    # EG:
        # print(obj1.func_name())
        # print(Class_name)
        # print(Class_name.x)




# -------- Class with nothing -------- 

# class Class_name ():
#     '''
#     Insert docstring
#     '''
#     # Insert attributes
#     # Insert methods
#     pass


# # -------- Instantiate Objects outside of class 

# obj1 = Class_name()
# obj2 = Class_name()

# # --------- Output:

# print(type(obj1))
# # returns: <class '__main__.Class_name'>
# print(obj1)
# # returns: <__main__.Class_name object at 0x0000023638B09F10>

# # --------- Use . to Define/Assign Attributes to the object without changing class (use __init__ to do in class)

# obj1.attr1 ="Kristy"
# obj1.attr2 = "Gray"

# # --------- Invoke for Output:

# print(obj1.attr1)
# # returns: Kristy
# print(type(obj1.attr2))
# # returns: <class 'str'>
# print(Class_name)
# # returns: <class '__main__.Class_name'>






























# NOTES:

# Class: Pet
# Objects / Instances: different dogs @ the store
    # Attributes: of dog
        # name, age, colour
    # Methods / Actions: of the dog --> behaviour of the object and/or doing something w/ the attributes
        # barking, changing the dog name

# ---------------------------

# class Class_name(arg1, arg2):
    # args are optional-----> class Class_name():
    # '''
    # docstring
    # '''
    # Insert Attributes
    # Insert Methods

# Instantiate Objects:
# object_name = Class_name(arg1a, arg2a)
# object_name2 = Class_name(arg1b, arg2b)
# ALT w/ no arguments ----> object_name = Class_name()
