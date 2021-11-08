import os

os.chdir("C:/Users/ferdi/OneDrive/Documents/Files_Exercise")

file = open("Book.txt","r")

files1 = file.read().lower()
files2 = open("Books.txt","w")

files2.writelines(files1)
file.close()
files2.close()

file = open("Books.txt","r")

def Book(text):
    text1 = ""
    for i in text:
        text1 += i
    return text1

def Book1(text1):
    data = {}
    for word in text1.split():
        data[word] = data.get(word,0)+1
    return data

lines = file.readlines()

text1 = Book(lines)

result = Book1(text1)

for key, value in result.items():
    if value <= 1:
        print(result[key],key)
    else:
        x = False