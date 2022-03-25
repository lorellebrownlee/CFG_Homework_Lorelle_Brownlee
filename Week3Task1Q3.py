#Question 3


#Your friend works for an antique book shop that sells books between 1800 and 1950
#and wants to quickly categorise books by the century and decade that they were
#written. Write a program that takes a year (e.g. 1872) and outputs the century and
#decade (e.g. "Eighteenth Century, Seventies")

#Take user input, asking what year the book was written in
publishing_year = input('What year was the book written in?')

#store the first 2 characters of the input string as the century, and the second from last character as the decade
century = publishing_year[:2]
decade = publishing_year[-2]

#create a dictionary of centuries and their long names
centuries = {
    '18': 'Nineteenth Century',
    '19': 'Twentieth Century',
    '20': 'Twenty First Century'
}

#create a dictionary of decades and their long names
decades = {
    '0': 'Noughties',
    '1': 'Teens',
    '2': 'Twenties',
    '3': 'Thirties',
    '4': 'Forties',
    '5': 'Fifties',
    '6': 'Sixties',
    '7': 'Seventies',
    '8': 'Eighties',
    '9': 'Nineties'
}

#print the century and the decade based on dictionary key value pairs
print('This book was published in the {:}, in the {:}.'.format((centuries[century]), (decades[decade])))


