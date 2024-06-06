#imports built in regular expression module from python library
import re

print ("Welcome to PigLatin")

#open txt file
with open("words.txt","r") as file:
    pig_latin = []

    #read each line in .txt
    for line in file:

        #read each word in text
        for word in line.split():
            #display words in .txt
            print(word)

            #remove special characters
            cleaned_word = re.sub(r"[^a-zA-Z]", "", word)

            if cleaned_word:
                #convert word to lowercase
                word = cleaned_word.lower()

                #checks if first letter is a vowel
                if word[0] in "aeiouAEIOU":
                    #suffixes "way" to original word
                    new_word = word + "way"

                else:
                    #get the first letter of the word
                    first = word[0]
                    #reads the original word from the second character, adds the first letter and "ay" to the end
                    new_word = word[1:] + first + "ay"

            print ("PigLatin: " + new_word)
            #add new_words to pig_latin array
            pig_latin.append(new_word)

#open text file in write mode
with open("pigLatin.txt", "w") as text_file:
    #Variable tracks whether text data was saved
    words_written = False

    #writes words to pigLatin.txt on seperate lines
    for word in pig_latin:
        text_file.write(word + "\n")
        #notify user of success
        words_written = True
    print("PigLatin conversion complete. Results written to 'pigLatin.txt'.")

    if not words_written:
        print("No words were written to 'pigLatin.txt'")

#Close file
text_file.close()