from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.cohort import Cohort
# first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ],
                "Maple"
            )

quinn.add_class("Painting")

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                "Spruce",
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )

students = [quinn, claire]
for student in students:
    print(student.summary())


cohort = Cohort(cohort_name = "C16", students = students)
print(cohort.class_list(class_name = "Maple"))
