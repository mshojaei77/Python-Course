'''
Write a function that takes a filename as input, removes any spaces from the filename and converts it to all lowercase characters.
The function should then check the extension of the file and print the MIME type of the file according to the following rules:

If the file has a ".gif" extension, print "image/gif"
If the file has a ".jpg" extension, print "image/jpg"
If the file has a ".jpeg" extension, print "image/jpeg"
If the file has a ".png" extension, print "image/png"
If the file has a ".pdf" extension, print "application/pdf"
If the file has a ".zip" extension, print "application/zip"
If the file has a ".txt" extension, print "text/plain"
Otherwise, print "application/octet-stream"
'''

# Get user input
filename = input("Name of the file: ")
# Remove spaces and make it all lower
new_filename = filename.lower().strip()
# Check types
if ".gif" in new_filename:
    print("image/gif")
elif ".jpg" in new_filename:
    print("image/jpg")
elif ".jpeg" in new_filename:
    print("image/jpeg")
elif ".png" in new_filename:
    print("image/png")
elif ".pdf" in new_filename:
    print("application/pdf")
elif ".zip" in new_filename:
    print("application/zip")
elif ".txt" in new_filename:
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
