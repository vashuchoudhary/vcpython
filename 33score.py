#Get the score from user in the range 0.0 and 1.0
score= input("Please enter the score in the range 0.0 and 1.0 :")

try :
    s=float(score)
except :
    print("ERROR: Please enter the floating value of score")
    quit()


if s > 1.0 :
    print("Error: Entered score is greated that 1.0")
elif s > 0.9 :
    print("A")
elif s>= 0.8 :
    print("B")
elif s>= 0.7 :
    print("C")
elif s>= 0.6 :
    print("D")
elif s < 0.6 :
    print("F")
