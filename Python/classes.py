"""
A class is a special data type which defines how to build a certain kind of object.
The class also stores some data items that are shared by all the instances of this class.
But no static variables!
"""
# classes
class ClassName(object):
    <statement-1>
    . . .
    <statement-N>

class MyClass(object):
    """A simple example class"""
    i = 12345
    def f(self):
        return self.i

class DerivedClassName(BaseClassName):
    <statement-1>
    . . .
    <statement-N>

class Thingy:
	"""This class stores an arbitrary object."""
	# Constructor
	def __init__(self, value):
		"""Initialize a Thingy."""
		self.value = value
	# method
	def showme(self):
		"""Print this object to stdout."""
		#print "value = %s" % self.value
		print("value =" + str(self.value))

class student:
    """A class representing a student."""
    def __init__(self,n, a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age
    def set_age(self, num):
        self.age = num


# instantiating objects
b = student("Bob", 21) #>>> b <__main__.student object at 0x010EC390>
b.full_name  # Access an attribute
b.get_age()  # Access a method
b.set_age(23)

# getattr(object_instance, string)
getattr(b, "full_name")    ## 'Bob'
getattr(b, "get_age")      ## <bound method student.get_age of <__main__.student object at 0x010EC390>>
getattr(b, "get_age")()    ## 21
getattr(b, "get_birthday") ## Traceback (most recent call last): File "<interactive input>", line 1, in <module>
                           ## AttributeError: 'student' object has no attribute 'get_birthday'

# hasattr(object_instance,string)
hasattr(b, "full_name") ## True
hasattr(b, "get_age")   ## True
hasattr(b, "get_birthday") ## False



# ================================
# Attributes
# ================================
"""
Data attribute: Variable owned by a particular instance of a class.
                Each instance can have its own different value for it.
                These are the most common kind of attribute.
Class attributes: Owned by the class as a whole.
                 All instances of the class share the same value for it.
                 Called “static” variables in some languages.
                 Good for class-wide constants or for building counter of how many instances of the class have been made.
"""

class teacher:
    """A class representing teachers."""
    def __init__(self,n):
        self.full_name = n # You create and initialize a data attribute inside of the __init__() method.
    def print_name(self):
        print( self.full_name )

class sample:
    x = 23                      # class attribute
    def increment(self):
        self.__class__.x += 1   # class attribute self.__class__.attr
        ##teacher.x += 1
#>>>
a.increment()
a.__class__.x #>>>24
a.teacher.x

class counter:
    overall_total = 0   # class attribute
    def __init__(self):
        self.my_total = 0   # data attribute
    def increment(self):
        counter.overall_total = \
        counter.overall_total + 1
        self.my_total = \
        self.my_total + 1

#>>>
a = counter()
b = counter()
a.increment()
b.increment()
b.increment()
a.my_total                 # 1
a.__class__.overall_total  # 3
b.my_total                 # 2
b.__class__.overall_total  # 3



# ================================
# Inheritance
# ================================

"""
A class can extend the definition of another class in order to use (or redefine) methods and attributes already defined in the previous one.
New class: “subclass.” Original: “parent” or “ancestor.”
Multiple inheritance is supported.
ex : class ai_student(student):
"""

class student:
    """A class representing a student."""
    def __init__(self,n, a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age
    def set_age(self, num):
        self.age = num

class ai_student (student):
    """A class extending student."""
    def __init__(self,n,a,s):
        student.__init__(self,n,a)  # note that here we put self
                                    # The only time you ever explicitly pass ‘self’ as an argument is when calling a method of an ancestor.
        self.section_num = s
    def get_age():
        print("Age: " + str(self.age))

# Special Built-In Methods and Attributes
# Built-In Members of Classes
# __doc__ __repr__

# Special Methods
__init__ : The constructor for the class.
__cmp__  : Define how == works for class.
__len__  : Define how  len( obj ) works.
__copy__ : Define how to copy a class.




class student:
 ...
  def __repr__(self):
    return “I’m named ” + self.full_name
 ...

>>> f = student(“Bob Smith”, 23)
>>> print f
I’m named Bob Smith
>>> f
“I’m named Bob Smith”

