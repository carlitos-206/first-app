import math
import sys 

print("\nWELCOME TO THE CALCULATOR APP\n")
print("\nTO START ENTER AN OPTION VALUE OR 9 FOR MENU OPTIONS\n") 
class app:
    sum = 0 
    def __init__(self, val):
        self.val = val
        if self.val == "1":
            print("IN THIS SECTION YOU HAVE THE ABILITY TO ADD TWO VALUES\n")
            def add(a,b):
                this_sum=a+b
                global sum 
                sum = this_sum
                print(f"\n = {sum}\n")
                return app(input("ENTER 2 TO ADD MORE OR ENTER A NEW MENU OPTION OR 9 FOR HELP: ")) 
            print(add(a=int(input("\nFIRST VALUE: ")), b=int(input("\nSECOND VALUE: "))))
        if self.val=="2":
            global sum
            if sum == 0:
                def add(a,b):
                    this_sum=a+b
                    global sum
                    sum = this_sum
                    print(f"\n = {sum}\n")
                    return app(input("\nENTER 2 TO ADD MORE OR ENTER A NEW MENU OPTION OR 9 FOR HELP: "))
                print("\nVALUES ARE NEEDED", add(a=int(input("\nFIRST VALUE: ")), b=int(input("\nSECOND VALUE: "))))
            else:
                print("\nADD ANOTHER VALUE TO THE SUM\n")
                def addMore(n):
                    global sum
                    this_sum = sum +n
                    sum = this_sum
                    print(f"\n = {sum}")
                    return app(input("\nENTER NEW MENU OPTION OR 9 FOR HELP: "))
            print(addMore(n=int(input(""))))
        if self.val == "3":
            print("\nWE ARE CLEARING THE GLOBAL SUM...\n")
            if sum > 0:
                sum-=sum
                print (f"\nTHE GLOBAL SUM IS NOW {sum}\n")
            elif sum == 0:
                print("THE SUM IS ALREADY 0")
            return app(input("\nENTER NEW MENU OPTION OR 9 FOR HELP; "))
        if self.val=="9":
            
            print(f"\nTHIS IS THE CURRENT SUM VALUE {sum}")
            print("""\nTHESE ARE THE OPTION THAT ARE MEANT FOR THE MENU:
            1 - ADDING TWO VALUES
            2 - ADD TO CURRENT SUM VALUE
            3 - CLEAR THE SUM 
            9 - HELP
            0 - EXIT""")
            return app(input("ENTER MENU OPTION: "))
        if self.val=="0":
            
            #This is how the app closes with sys.exit() function 
            
            sys.exit("\nTHANK YOU, GOODBYE\n")
        else:
            print("\nENTER A PROPER OPTION OR 9 FOR MENU OPTIONS\n")
            return app(input("\nENTER MENU OPTION: "))
user=app(val=input())

#this a tes
