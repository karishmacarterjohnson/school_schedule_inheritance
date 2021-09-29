class Cohort:
    def __init__(self,cohort_name,students=None):
        self.cohort_name = cohort_name
        self.students = students if students is not None else []

    def student_summaries(self):
        for student in self.students:
            print(student.summary())

    def homeroom_class_list(self,homeroom_name):
        return [student.name for student in self.students if student.class_name == homeroom_name]

    def class_list(self, class_name):
        return [student.name for student in self.students if class_name in student.classes]