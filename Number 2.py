import os

os.chdir("C:/Users/ferdi/OneDrive/Documents/Files_Exercise")

file = open("Book.txt","r")
files = open("Rebook.txt","w")
file = file.readlines()

count = 0

for sen in file:
    count += 1
    files.write("{:2d} {}".format(count, sen))

files.close()