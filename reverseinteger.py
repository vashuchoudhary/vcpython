class Solution:
    def reverse(self,x: int):
        print("The value of X passed:", x)
        if x >= pow(2,31) or x <= -pow(2,31) :
            print("X has exceeded the value")
            return
        xstring = str(x)
        return xstring[::-1]

P1 = Solution()
xinput = int(input("Enter the value of X: "))
print(P1.reverse(xinput))
