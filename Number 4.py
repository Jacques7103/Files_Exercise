import re
import os

os.chdir("C:/Users/ferdi/OneDrive/Documents/Files_Exercise")
file = open("Test.txt","w")

inp = ("Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.")
rum = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", inp)

count = 0

for i in rum:
    file.write(i)
    count += 1
    if count < len(rum):
        file.write("\n")
    else:
        False