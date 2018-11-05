from functools import total_ordering
# Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。


class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


@total_ordering
class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(student: %s, %s, %s)' % (self.name, self.gender, self.score)

    __repr__ = __str__

    # Python3
    def __lt__(self, other):
        return (self.score, self.name) < (other.score, other.name)

    def __eq__(self, other):
        return (self.score, self.name) == (other.score, other.name)

    # Python2, __cmp__ is discarded from Python3
    # def __cmp__(self, s):
    #     if self.score > s.score:
    #         return -1
    #     elif self.score < s.score:
    #         return 1
    #     else:
    #         if self.name < s.name:
    #             return -1
    #         elif self.name > s.name:
    #             return 1
    #         else:
    #             return 0


s = Student('Bob', 'male', 88)
print(s)

L = [Student('Tim', 'male', 99), Student(
    'Bob', 'male',  88), Student('Alice', 'male',  99)]

print(sorted(L))
