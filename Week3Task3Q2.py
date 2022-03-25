#Task 3 Question 2: This program should save my data to a file, but it doesn't work when I run it. What
#is the problem and how do I fix it?

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)

#Answer: The problem is that the file handling method, detailed in the open() parameters, is set to ‘r’, which is read only and will return an error if the file does not exist.
# The file handling method should be set to ‘w’ which will write to the file and create the file if it does not exist.
# The code above has been corrected.
