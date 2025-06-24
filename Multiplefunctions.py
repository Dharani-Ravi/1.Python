class MultipleFunctions():
    def Subfields():
            print("Sub-fields in AI Are:")
            print("machine Learning")
            print("Neural Networks")
            print("Vision")
            print("robotics")
            print("Speech Processing")
            print("Natural Language Processing")
    def OddEven():
        num=int(input("Enter the number:"))
        if (num%2==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    def eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=="Male" and Age<=21):
            print("Eligible")
        elif(Gender=="Female" and Age<=18):
            print("Eligible")
        else:
            print("Not Eligible")
    def percentage():
            Subject1=int(input("Subject1="))
            Subject2=int(input("Subject2="))
            Subject3=int(input("Subject3="))
            Subject4=int(input("Subject4="))
            Subject5=int(input("Subject5="))
            Total=(Subject1+Subject2+Subject3+Subject4+Subject5)
            Percentage=(Total/5)
            print("Total:",Total)
            print("Percentage:",Percentage)
    def triangle():
            Height=int(input("Height"))
            Breadth=int(input("Breadth"))
            Area=(Height*Breadth)/2
            print("Area of triangle:",Area)
            Height1=int(input("Height1"))
            Height2=int(input("Height2"))
            Breadth=int(input("Breadth"))
            Perimeter=(Height1+Height2+Breadth)
            print("Perimeter of Triangle:",Perimeter)