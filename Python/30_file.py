# path - X:\VScode\PYTHON\07_Junk_Code\data.txt



with open("X:\\VScode\\PYTHON\\07_Junk_Code\\data.txt", 'w') as data:
    data.write("Hello\nHow are you...")

# print(type(content))
# print(content)
with open("X:\\VScode\\PYTHON\\07_Junk_Code\\data.txt", 'r') as data:
    content = data.read()

print(type(content))
print(content)


# types of file operation 
'''
'r' = Reading 
'w' = Writing (remove existing content and add new)
'x' = creating new and open for writing 
'a' = writing and appending
'b' = binary mode
't' = text mode
'+' = open disk for update (r & w)
'''

# 'r' — Read (file must exist)
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# 'w' — Write (delete old content, write new)
with open("file.txt", "w") as f:
    f.write("This overwrites everything.\n")

# 'x' — Create new file and write (fails if file exists)
with open("newfile.txt", "x") as f:
    f.write("File created successfully.\n")

# 'a' — Append (add at the end)
with open("file.txt", "a") as f:
    f.write("This line is appended.\n")

# 'b' — Binary mode
with open("image.bin", "wb") as f:
    f.write(b"\x48\x65\x6c\x6c\x6f")


# Read binary:

with open("image.bin", "rb") as f:
    data = f.read()
    print(data)

# 't' — Text mode (default)
with open("textfile.txt", "wt") as f:
    f.write("Text mode is default.\n")

# '+' — Read and Write (update mode)

# Read + Write

with open("file.txt", "r+") as f:
    print(f.read())
    f.write("\nUpdated content.")


# Write + Read (overwrite first)

with open("file.txt", "w+") as f:
    f.write("New content.\n")
    f.seek(0)
    print(f.read())


# Append + Read

with open("file.txt", "a+") as f:
    f.write("\nAppending with read access.")
    f.seek(0)
    print(f.read())

# with keyword (no need to close the file.)

# deleting file 
import os

os.remove("data.txt") # we can perform different operation using OS module 






