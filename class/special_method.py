"""[summary]
    测试 special method (特殊方法)
        __str__(self) 显示类信息给用户
        __repr__(self) 显示类信息给开发人员
        __lt__(self, other) 比较 self 是否小于 other
        __eq__(self, other) 比较 self 是否等于 other

Returns:
    [type] -- [description]
    None
"""

from functools import total_ordering


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
