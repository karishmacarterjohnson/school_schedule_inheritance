class Cohort:
    def __init__(self,cohort_name,students=None):
        self.cohort_name = cohort_name
        self.students = students if students is not None else []

    def student_summaries(self):
        for student in self.students:
            print(student.summary())

    def class_list(self,class_name):
        return [student.name for student in self.students if student.class_name == class_name]
