#define is_raining as user input as response to question

is_raining = input('Is it raining? y/n:')

#check if response is y or n and respond appropriately
for i in range(len(is_raining)):
    if is_raining == 'y':
        print('Take an umbrella')
    elif is_raining == 'n':
        print("You don't need an umbrella")
    else:
        print("Sorry, I don't understand")
