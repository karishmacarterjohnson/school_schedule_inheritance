from .student import Student

# add MiddleSchoolStudent here

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, class_name,
        gets_transportation=False):

        super().__init__(name, grade, classes, class_name)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()

        return "\n".join((student_summary, transportation_message))

    def display_transportation_message(self):
        gets_message = "gets" if self.gets_transportation else "doesn't get"
        return f"{self.name} {gets_message} transportation"