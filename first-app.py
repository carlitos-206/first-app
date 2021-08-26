import math
print("\nWELCOME TO THE CALCULATOR APP\n")
print("\nTO START ENTER AN OPTION VALUE OR 9 FOR MENU OPTIONS\n") 
class app:
    def __init__(self, val):
        self.val = val
        if self.val == "1":
            print("IN THIS SECTION YOU HAVE THE ABILITY TO ADD TWO VALUES\n")
            def add(a,b):
                sum = a+b
                print(f"\n = {sum}\n")
                return app(input("ENTER NEW MENU OPTION OR 9 for HELP: ")) 
            print(add(a=int(input("\nFIRST VALUE: ")), b=int(input("\nSECOND VALUE: "))))
        if self.val=="9":
            print("""THESE ARE THE OPTION THAT ARE MEANT FOR THE MENU:
            1 - ADDING TWO VALUES
            9 - HELP
            0 - EXIT""")
            return app(input("ENTER MENU OPTION: "))
        if self.val=="0":
            print("\nGOODBYE\n")
            return None
        #if self.val!=int:
         #   print("\nTHE VALUE MUST BE A NUMBER, FOR HELP 9")
          #  return app(input("ENTER MENU OPTION: "))
        else:
            print("\nENTER A PROPER OPTION OR 9 FOR MENU OPTIONS\n")
            return app(input("ENTER MENU OPTION: "))
user=app(val=input())
