import re


fname= input("Enter filename: ")
fhand= open(fname)
sum = 0
for line in fhand:
    number = re.findall('[0-9]+', line.rstrip())
    #print(number)
    for add in number:
        sum = sum + int(add)
print(sum)
