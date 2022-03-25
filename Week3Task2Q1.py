#Question:

#I have a list of things I need to buy from my supermarket of choice.

#shopping_list = [
#"oranges",
#"cat food",
#"sponge cake",
#"long-grain rice",
#"cheese board",
#]
#print(shopping_list[1])


#I want to know what the first thing I need to buy is. However, when I run the program
#it shows me a different answer to what I was expecting? What is the mistake? How
#do I fix it.




###Answer: The current code accesses the list index 1, which is ‘cat food’ as indices start at 0 in python. If we want to access the first element in the list, we can either change the list index to 0 in the print call, or we can use slicing syntax. Below is the code using slicing syntax and showing the output.
shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]
print(shopping_list[:1])

#output: ['oranges']
