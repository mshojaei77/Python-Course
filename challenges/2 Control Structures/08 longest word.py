# Write a program that prompts the user to enter a sentence and then uses a while loop to print out the longest word in the sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""

i = 0
while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    i += 1

print("The longest word in the sentence is:", longest_word)
