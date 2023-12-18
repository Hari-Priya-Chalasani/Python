# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.



file = input("File name: ")
file_lower = file.lower()

if file_lower.endswith(".gif"):
    print("Image/gif")
elif file_lower.endswith(".jpg") or file_lower.endswith(".jpeg"):
    print("Image/jpeg")
elif file_lower.endswith(".png"):
    print("Image/png")
elif file_lower.endswith(".pdf"):
    print("pdf file")
elif file_lower.endswith(".txt"):
    print("text")
elif file_lower.endswith(".zip"):
    print("zip")
else:
    print("application/octet-stream")