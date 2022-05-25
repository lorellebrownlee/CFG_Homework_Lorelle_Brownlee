"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student's full name and student's id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called 'specialization' and course grades.

The child class 'generate_id' method should override its parent method to add the suffix 'NANO'
in front of the id.

New methods 'add_new_grade' and 'get_course_grades' should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

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

    @staticmethod
    def generate_id(self):

        self.student_id = random.randint(1000,10000)

        return str(self.student_id)

        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "


    # create a method to fetch student's full name
    def get_fullname(self):
        self.name = input('Please enter first name:')
        self.surname = input('Please enter surname')
        self.full_names[self.name] = self.surname
        print(self.full_names)


class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, student_id, specialisation, course_grades):
        super().__init__(name, surname, age, email, student_id)
        self.specialisation = specialisation
        self.student_id = student_id
        self.course_grades = dict()
        self.course_grades[student_id] = course_grades


    @staticmethod
    def generate_id(self):
        
        student_id = str('NANO' +str(random.randint(1000,10000)))
        print(student_id)

    ##add new grade instead here
    def add_new_grade(self):
        subject = input('Please enter subject:')
        grade = input('Please enter grade:')
        
        self.subjects[self.specialisation]['extra_subject'] = subject
        self.course_grades[self.student_id]['extra_subject'] = grade
        print(self.subjects[self.specialisation]['subject_1'])
        print(self.course_grades)


    def get_course_grades(self):
        print(self.course_grades[self.student_id])  



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""



#function to find fibonacci number
def fibonacci(limit):
    
    if limit == 0:
        return 0
    elif limit == 1 or limit == 2:
        return 1
    else:
        return fibonacci(limit - 1) + fibonacci(limit - 2)

#function to find the fibonacci numbers in sequence up to a given limit and to attach them to indices in a dictionary
def even_fibonacci_sum(limit):
    index = 0
    indices = []
    even_nums = []
    values = []
    for i in range(0, limit):
        indices.append(index)
        values.append(fibonacci(i))
        index = index + 1
    indices_values = {indices[n]: values[n] for n in range(len(indices))}
    print('The indices and fibonacci values are:', indices_values)

    #for each index up to the limit, if the fibonacci number corresponding to the index is an even number, 
    #add it to the total sum then return the final sum
    for j in indices:
        limit = j
        if fibonacci(limit) % 2 == 0:
            even_nums.append(fibonacci(limit))
    return sum(even_nums)

# ##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

#define function
def is_valid_subsequence(array1, sequence1):

    #set the indices to 0 to start
    index_of_array = 0
    index_of_sequence = 0

    #while the index of the array is less than the length of the array and the index of the sequence is less than
    #the length of the sequence if the character in the sequence matches the character in the array, add 1 the index and move
    #on to the next character in each
    while index_of_array < len(array1) and index_of_sequence < len(sequence1):
        if sequence1[index_of_sequence] == array1[index_of_array]:
            index_of_sequence = index_of_sequence + 1
        index_of_array = index_of_array + 1

    #if the index number is equal to the length of sequence, it is assumed all characters in the sequence are also in the 
    #array in the same order so return True
    return index_of_sequence == len(sequence1)
            


###tests###


array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]
print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]
print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]
print(is_valid_subsequence(array3, sequence3))  # TRUE


"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""








