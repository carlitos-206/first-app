import math
print("\nWELCOME TO THE CALCULATOR APP\n")
print("\nTO START ENTER AN OPTION VALUE OR 9 FOR MENU OPTIONS\n") 
class app:
    def __init__(self, val):
        self.val = val
        if self.val == 1:
            print("IN THIS SECTION YOU HAVE THA ABILITY TO ADD TWO VALUES\n")
            def add(a,b):
                sum = a+b
                print(sum,"\n")
                return app(int(input("ENTER NEW MENU OPTION OR 0 for HELP: "))) 
            print(add(a=int(input("FIRST VALUE: \n")), b=int(input("SECOND VALUE: \n"))))
        if self.val==9:
            print("""THESE ARE THE OPTION THAT ARE MEANT FOR THE MENU:
            1 - ADDING TWO VALUES
            9 - HELP
            0 - EXIT""")
            return app(int(input("ENTER MENU OPTION: ")))
        if self.val==0:
            return print("thanks") 
user=app(val=int(input()))
