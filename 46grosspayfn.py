def computepay(h,r) :
    if h<=40 :
        pay=h*r
    else :
        morehours= h-40
        pay= 40*r + morehours*1.5*r

    return pay

hrs = input("Enter Hours:" )
rate = input("Enter Rate:" )

try:
    h=float(hrs)
    r=float(rate)
except:
    print("ERROR: Please enter the numberic value for hours and rate")
    quit()

p = computepay(h,r)
print("Pay :",p)
