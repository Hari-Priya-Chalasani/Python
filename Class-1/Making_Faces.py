word = input("Enter the text: ")
new_word = word.replace(":)", "🙂").replace(":(", "🙁")

# Check if any replacements were made
if new_word != word:
    print("Replaced:", new_word)
else:
    print("No replacements made. Original text:", word)
