# import datetime

# class Person:

#     Titles = ('Dr', 'Mr', 'Mrs', 'Ms')
#     def __init__(self, title, name, surname, birthday, address, telephone, email):
#         if title not in self.Titles:
#             raise ValueError("%s is not a valid title." %title) 
#         self.title = title
#         self.name = name
#         self.surname = surname
#         self.birthday = birthday
#         self.address = address
#         self.telephone = telephone
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         print(today)
#         print(type(today))
#         print(today.month)
#         print(today.year)
#         age = today.year - self.birthday.year

#         if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
#             age -= 1

#         self._age = age
#         if hasattr(self, "_age"):
#             return self._age
#         return age

# person = Person(
#     "Mr",
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12),
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jone.doe@example.com"
# )

# person.pets = ["cat", "dog", "bird"]

# print(person.title)
# print(person.name)
# print(person.email)
# print(person.age())
# # print(person.pets[2])

class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): # instance method
        # instance object accessible through self
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
        # no parameter for class or instance object
        # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]


jane = Person("Jane", "Smith")

print(jane.fullname())

print(jane.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))

print(jane.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))