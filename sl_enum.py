from enum import Enum
from enum import Enum, unique

"""
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

"""


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print("ok")
else:
    print('failed')
