import os

os.chdir("C:/Users/ferdi/OneDrive/Documents/Files_Exercise")
file = open("Book.txt","r")
file = file.read()

sumt = sum([len(file) for files in file]) / len(file)

file = file.split()

wordt = sum([len(file) for files in file]) / len(file)

print(sumt/wordt)