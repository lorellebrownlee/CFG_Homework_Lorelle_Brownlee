#define function isPalindrome with parameter my_string
def isPalindrome(my_string):
    #loop through the index of each element in the string
    for i in range(len(my_string)):
        #declare rev_string, a string that is the rverse of my_string
        rev_string = my_string[::-1]
        #set the index for my_string to start from 0 and be called forward_index
        forward_index = 0
        #set the index for rev_string to start from 0 and be called rev_index
        rev_index = 0
        #while the indices of the two strings are the same, if the elements at that index in each of the two strings don't match
        #then return false
        while rev_index == forward_index:
            if my_string[forward_index] != rev_string[rev_index]:
                return False
                #increment both indices by 1 to move to next index
                forward_index += 1
                rev_index += 1
            return True


print(isPalindrome('hannah'))



