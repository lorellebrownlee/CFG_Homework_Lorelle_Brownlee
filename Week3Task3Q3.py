#Question 3

#Here is a snippet of Elton John’s song “I’m Still Standing”

#You could never know what it's like
#Your blood like winter freezes just like ice
#And there's a cold lonely light that shines from you
#You'll wind up like the wreck you hide behind that mask you use
#And did you think this fool could never win?
#Well look at me, I'm coming back again
#I got a taste of love in a simple way
#And if you need to know while I'm still standing, you just fade away
#Don't you know I'm still standing better than I ever did
#Looking like a true survivor, feeling like a little kid
#I'm still standing after all this time
#Picking up the pieces of my life without you on my mind
#I'm still standing (Yeah, yeah, yeah)
#I'm still standing (Yeah, yeah, yeah)


#Tasks:

#1.Write the lyrics to a new file called song.txt
#2.Check that a file has been created successfully.
#3. The read lines from this file and print out ONLY those lines that have a word
#‘still’ in them.



# set the song lyrics to the string 'lyrics'
lyrics = """You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)"""

#write the lyrics into a text file called 'song.txt'
with open('song.txt', 'w') as song:
   song.write(lyrics)

# create a string called 'substring' containing the word 'still' as a string
substring ='still'

#open song.txt for reading and for each line, if it contains the substring 'still', print the line
with open('song.txt', 'r') as song:
   lines_with_still = song.readlines()
   for line in lines_with_still:
       if substring in line:
           print(line)
