'''
User Class
'''


class User:
    '''
    User
    '''
    name: str
    age: int
    email: str

    def __init__(self, name, age, email: str):
        self.name = name
        self.age = age
        self.email = email

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):
        return self.name
