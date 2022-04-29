# TASK 2

# Write a base class to represent a student. Below is a starter code.

# Feel free to add any more new features to your class.

# As a minimum a student has a name and age and a unique ID.

# superclass Student
class Student:

    def __init__(self, name, age, id):

        self.name = name

        self.age = age

        self.id = id
        # dictionary of subjects contained within each respective course stream
        self.subjects = {
            'Data Science': {'subject_1':'MLAlgorithms', 'subject_2':'Time Series Analysis', 'subject_3': 'Data and SQL', 'subject_4':'Algebra', 'subject_5':'Visualisations'},
            'Software Engineering': {'subject_1':'Python', 'subject_2':'Dictionaries', 'subject_3':'Object Oriented Programming', 'subject_4':'Regex and Lambda', 'subject_5':'Recursive functions'}}
        #dictionary of student grades by subject and student id
        self.student_grades = {
            '001': {'subject_1': 0.79, 'subject_2': 0.58, 'subject_3': 0.79, 'subject_4': 0.67, 'subject_5': 0.94 },
            '002': {'subject_1': 0.61, 'subject_2': 0.79, 'subject_3': 0.45, 'subject_4': 0.90, 'subject_5': 0.74 },
            '003': {'subject_1': 0.50, 'subject_2': 0.46, 'subject_3': 0.98, 'subject_4': 0.56, 'subject_5': 0.65 }
        }

    #     create a method to view all subjects taken by a student
    def view_subjects(self):
        student_subjects =self.subjects[self.stream]
        for subject in student_subjects:
            print(student_subjects[subject])

        #     create a method  (and a new variable) to get student's overall mark (use average)
    def total_grade(self):

        total_grade = 0

        self.grades = self.student_grades[self.id]

        for subject in self.grades:
            total_grade = total_grade + self.grades[subject]
        final_grade = total_grade / len(self.grades.keys())
        print('The overall grade is: {:.0%}'.format(final_grade))

# Create a new subclass from student to represent a concrete student doing a specialization, for example:

class software_Student(Student):

    def __init__(self, name, age, id, stream):
        super().__init__(name, age, id)
        self.stream = stream

    #method to add subject and grade to dictionaries
    def add_subject(self):
        additional_subject = input('What extra class did the student take?')
        add_subject_grade = input('What was the score for this class?')
        self.subjects[self.stream].update(additional_subject = additional_subject)
        self.student_grades[self.id].update(additional_subject = float(add_subject_grade))
        print(self.subjects[self.stream])
        print(self.student_grades[self.id])
        print('The overall grade with the additional subject will be recalculated.')
        self.total_grade_add()

    #method to remove subject and grade from dictionaries
    def drop_subject(self):
        dropped_subject = input('What class did the student drop?')
        new_subj_dict = {key:val for key, val in self.subjects[self.stream].items() if val != dropped_subject}
        self.mini_grades_list = {key2:val2 for key2, val2 in self.student_grades[self.id].items() if key2 in new_subj_dict}
        print(new_subj_dict)
        print(self.mini_grades_list)
        print('The overall grade after dropping a subject will be recalculated.')
        self.total_grade_drop()

    #     create a method  (and a new variable) to get student's overall mark (use average) after adding a new subject
    def total_grade_add(self):
        total_grade = 0
        self.grades = self.student_grades[self.id]

        for subject in self.grades:
            total_grade = total_grade + self.grades[subject]
        final_grade = total_grade / len(self.grades.keys())
        print('The overall grade is: {:.0%}'.format(final_grade))

    #     create a method  (and a new variable) to get student's overall mark (use average) after removing a subject
    def total_grade_drop(self):
        total_grade = 0
        self.grades_drop = self.mini_grades_list

        for subject in self.grades_drop:
            total_grade = total_grade + self.grades_drop[subject]
        final_grade = total_grade / len(self.grades_drop.keys())
        print('The overall grade is: {:.0%}'.format(final_grade))

#creating objects of child class
student_1 = software_Student('Sarah Jones', 22, '001', 'Data Science')
student_2 = software_Student('Henrietta Izaz', 24, '002', 'Software Engineering')
student_3 = software_Student('Kelly Kohn', 28, '003', 'Software Engineering')

#calling child class methods
student_1.view_subjects()

student_1.total_grade()

student_1.add_subject()

student_1.drop_subject()

#to show that software_Student class is a subclass of Student
print('software_Student is a sub class of Student: ',issubclass(software_Student, Student))



