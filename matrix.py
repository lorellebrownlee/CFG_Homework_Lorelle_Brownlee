"""
SEARCH IN MATRIX
--------

You are given a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


#declare function with arguments 'matrix' and 'target'
def search_in_matrix(matrix, target):
    index_list = []
    #enumerate the lists within the matrix to give each list an index, with the list itself acting as value
    for index, value in enumerate(matrix): 
        #if the target number is in a list, then enumerate that list giving each element in the list further indices and values
        if target in value:
            for subindex, subvalue in enumerate(value):
                #if a value within the list in the matrix is equal to the value of the target number, then append the row value of target ('index') and column value of target ('subindex') to the empty list
                if target == subvalue: 
                   index_list.append(index)
                   index_list.append(subindex)
    #if the list is not empty at the end of the process, return the list, else return [-1, -1]               
    if index_list != []:
        return index_list
    else: 
        return [-1, -1]
    
  

print(search_in_matrix([
[1,4,7,120,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
], 100))
