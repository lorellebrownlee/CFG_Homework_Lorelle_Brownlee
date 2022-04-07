class TwoNumSum:
  def __init__(self, my_numbers, target_sum):
    self.my_numbers = my_numbers
    self.target_sum = target_sum

#define the function TwoNumFunc

  def TwoNumFunc(my_param):

    #set counter to 0

    count = 0

    #search list for first element

    for i in my_param.my_numbers:

        #search list for second element

        for j in my_param.my_numbers:

            #if the sum of two elements equals the target sum

            if j + i == my_param.target_sum:

                #add 1 to the count

                count = count + 1

                #print the values that sum to target sum

                print([i, j])

    #if count = 0 meaning no two values summed to the target sum, print an empty array

    if count == 0:

        print([])

my_inputs= TwoNumSum([3,5,-4,8,11,1,-1,24, -14], 10)

my_inputs.TwoNumFunc()

