#User will enter a number
smallest = None
largest = None
wrongip = "temp"
while True:

    try :
        num = input("Enter Number: ")
        if num == "done" :
            break
        num= int(num)
    except :
        wrongip= "Invalid Input"
        continue

    if smallest is None:
       smallest = num
       print("Smallest number value:",smallest)
    if largest is None:
       largest = num
       print("Largest number value:",largest)
    if smallest > num :
        smallest = num
    if largest < num :
        largest = num
        print("Largest number test value:",largest)
if wrongip== "Invalid Input" :
    print (wrongip)

print ("Maximum is ", largest)
print ("Minumum is", smallest)
