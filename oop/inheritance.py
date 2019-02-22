# Doc Desc
# 简单继承样例, 及多态

from .definition import Person


class Teacher(Person):
    def __init__(self, name, gender, course):
        # 调用父类的方法
        super(Teacher, self).__init__(name, gender)
        self.course = course

    # 多态
    def show_props(self):
        return 'I am a teacher teaching ' + self.course + '. ' + ' '.join(['Hello', self.name, '(', self._sex, ')'])


def main():
    t1 = Teacher('Bob', 'male', 'Math')
    print("Instance ", t1.__class__, ": ", t1.show_props())


if __name__ == '__main__':
    main()
