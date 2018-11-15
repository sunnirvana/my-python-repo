# Doc Desc
# 使用property关键字(decorator)定义属性


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # 注意: 第一个score(self)是get方法，用@property装饰，
    # 第二个score(self, score)是set方法，用@score.setter装饰，
    # @score.setter是前一个@property装饰后的副产品。

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    # 如果没有定义set方法，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。
    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score < 60:
            return 'C'
        else:
            return 'B'


s = Student('Bob', 59)
print('source: %s, grade: %s' % (s.score, s.grade))
s.score = 60
print('source: %s, grade: %s' % (s.score, s.grade))
s.score = 99
print('source: %s, grade: %s' % (s.score, s.grade))

try:
    # grade 是只读属性, 不能赋值, 如下操作会报错误
    s.grade = 'D'
except AttributeError:
    print('s.grade = "D" raise Error: ', AttributeError)
