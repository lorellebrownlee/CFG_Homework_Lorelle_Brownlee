# Design a parent class called CFGStudent.

# It should have general attributes like name, surname, age, email, student id
# and methods to fetch student’s full name and student’s id.

# Design a child class called NanoStudent, which  inherits from CFGStudent class.
# This class should have exactly the same attributes as its parent class,
# as well as an additional one called ‘specialization’ and course grades.

# The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
# in front of the id.

# New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
# You can use  it as a skeleton code for your classes OR adjust it and create your own.

class CFGStudent():

    def __init__(self, name, surname, age, email, student_id):

        self.name = name

        self.surname = surname

        self.age = age

        self.email = email

        self.student_id = student_id

        self.student_id_list = []

        self.subjects = {
            'Data': {'subject_1':'Algorithms', 'subject_2':'Graphs', 'subject_3': 'Data and SQL', 'subject_4':'Classification'},
            'Software': {'subject_1':'OOP', 'subject_2':'Algorithms', 'subject_3':'Flask', 'subject_4':'Sorting'}}
        #dictionary of student grades by subject and student id


        self.full_names = dict()
        

    # create a method to fetch student's full name
    def fetch_full_name(self):
        self.name = input('Please enter first name:')
        self.surname = input('Please enter surname')
        self.full_names[self.name] = self.surname
        print(self.full_names)
        


    #method to fetch student id
    def generate_id(self):
        self.student_id = self.student_id
        print(self.student_id)


# child class

class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, student_id, specialisation, course_grades):
        super().__init__(name, surname, age, email, student_id)
        self.specialisation = specialisation
        self.student_id = student_id
        self.course_grades = dict()
        self.course_grades[student_id] = course_grades



    # method to add new student id overriding parent class generation of student id and add suffix 'NANO'
    def generate_id(self):
        
        self.student_id = self.student_id +'NANO'
        print(self.student_id)

    ##add new grade instead here
    def add_new_grade(self):
        subject = input('Please enter subject:')
        grade = input('Please enter grade:')
        
        self.subjects[self.specialisation]['extra_subject'] = subject
        self.course_grades[self.student_id]['extra_subject'] = grade
        print(self.subjects[self.specialisation]['subject_1'])
        print(self.course_grades)

    #method to get student's grades
    def get_course_grades(self):
        print(self.course_grades[self.student_id])  



# #objects
student_1 = NanoStudent('Lisa', 'Smith', 31, 'lisasmith@gmail.com', '001', 'Data', {'subject_1':'A','subject_2': 'C', 'subject_3':'B', 'subject_4':'A'})


# #calling methods
student_1.fetch_full_name()
student_1.generate_id()
student_1.add_new_grade()
student_1.get_course_grades()

########################################################

def fibonacci(limit):
    sums =[]
    indices = []
    if limit == 0:
        return 0

    elif limit == 1 or limit == 2:
        return 1

    else:
        return fibonacci(limit - 1) + fibonacci(limit - 2)

indices = []
even_sums = []
values = []
index = 0
limit = 20

for i in range(0, limit):
    indices.append(index)
    values.append(fibonacci(i))
    index = index + 1
indices_values = {indices[n]: values[n] for n in range(len(indices))}
print('The indices and fibonacci values are:', indices_values, '\nThe even values are:')


for j in indices:
    limit = j
    if fibonacci(limit) % 2 == 0:
        print(fibonacci(limit))
        even_sums.append(fibonacci(limit))
print('The sum of all even values in the sequence is:', sum(even_sums))
    

#####################################################


"""Given two non-empty arrays of integers, write a function that determines whether the second array is a 
subsequence of the first one. NB A subsequence in an array in this case is a set of numbers that aren't 
necessarily adjacent in the array, but are in the same order as they appear in the array."""

def is_subsequence(array1, sequence1):

    index_of_array = 0
    index_of_sequence = 0

    while index_of_array < len(array1) and index_of_sequence < len(sequence1):
        if sequence1[index_of_sequence] == array1[index_of_array]:
            index_of_sequence = index_of_sequence + 1
        index_of_array = index_of_array + 1

    return index_of_sequence == len(sequence1)
            



  

#driver code    
print(is_subsequence([5,1,22,25,6,-1,8,10], [25]))

###tests###


# array1 = [5,1,22,25,6,-1,8,10]
# sequence1 = [1,6,-1,-2]
# print(is_valid_subsequence(array1, sequence1))  # FALSE


# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
# print(is_valid_subsequence(array2, sequence2))  # TRUE


# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
# print(is_valid_subsequence(array3, sequence3))  # TRUE