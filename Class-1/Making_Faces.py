#Taking the Input text with  emoticons.
word = input("Enter the text: ")

#replacing emoticons with emojis
new_word = word.replace(":)", "🙂").replace(":(", "🙁")

#printing the word or sentence with replaced emojis
print(new_word)
