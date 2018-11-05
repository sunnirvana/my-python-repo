class Person(object):
    def __init__(self):
        print("Person init")
    pass


class Student(Person):
    def __init__(self):
        print("Student init")
    pass


class Teacher(Person):
    def __init__(self):
        print("Teacher init")
    pass


class SkillMixin(object):
    def __init__(self):
        print("SkillMixin init")
    pass


class BasketballMixin(SkillMixin):
    def __init__(self):
        print("BasketballMixin init")

    def skill(self):
        return 'basketball'


class FootballMixin(SkillMixin):
    def __init__(self):
        print("FootballMixin init")

    def skill(self):
        return 'football'


class BStudent(Student, BasketballMixin):
    def __init__(self):
        # super(BStudent, self).__init__()
        Student.__init__(self)
        BasketballMixin.__init__(self)
    pass


class FTeacher(Teacher, FootballMixin):
    def __init__(self):
        super(FTeacher, self).__init__()
    pass


s = BStudent()
print(s.skill())
t = FTeacher()
print(t.skill())
