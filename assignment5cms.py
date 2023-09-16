def back():
     again=int(input("enter 5 to go back to the main page"))
     if again==5:
          main()
def main():
    print("Welcome to college of engineering \n")
    f=open("college of engineering.txt","r")
    txt=f.read()
    f.close()
    print(txt)
   
   
    def cse():
                print("this is computer science and engineering department")
                checkdetails=int(input("press 1 to know about the course:"))
                if checkdetails==1:
                    print("this course about the computer hardwares and software and networking concepts")
                else:
                    print("enter the mentioned number")
                    #fees details
                semfees=int(input("press 1 to know semfees details:"))
                if semfees:
                    print(f"50000 per semester", "full fees>>",{50000*8} )
                else:
                    print("enter the correct option")
                busfees=int(input("press 2 to know bus fees details:"))
                if busfees:
                    print("15000 per semester")
                else:
                    print("enter the correct number")
                    
                admission=int(input("press 1 to admission:"))
                if admission:
                    print("your application is submitted")
                else:
                    print("please press 1")
    def eee():
                print("this is electrical and eletronical and engineering department")
                checkdetails=int(input("press 1 to know about the course:"))
                if checkdetails==2:
                    print("this course about the computer hardwares and software and networking concepts")
                else:
                    print("enter the mentioned number")
                    #fees details
                semfees=int(input("press 1 to know semfees details:"))
                if semfees:
                    print(f"70000 per semester", "full fees>>",{70000*8} )
                else:
                    print("enter the correct option")
                busfees=int(input("press 2 to know bus fees details:"))
                if busfees:
                    print("15000 per semester")
                else:
                    print("enter the correct number")
                    
                admission=int(input("press 1 to admission:"))
                if admission:
                    print("your application is submitted")
                else:
                    print("please press 1")
    def ece():
                print("this is elctrical and communication engineering department")
                checkdetails=int(input("press 1 to know about the course:"))
                if checkdetails==3:
                    print("this course about the computer hardwares and software and networking concepts")
                else:
                    print("enter the mentioned number")
                    #fees details
                semfees=int(input("press 1 to know semfees details:"))
                if semfees:
                    print(f"80000 per semester", "full fees>>",{80000*8} )
                else:
                    print("enter the correct option")
                busfees=int(input("press 2 to know bus fees details:"))
                if busfees:
                    print("15000 per semester")
                else:
                    print("enter the correct number")
                    
                admission=int(input("press 1 to admission:"))
                if admission:
                    print("your application is submitted")
                else:
                    print("please press 1")
    def mech():
                print("this is computer science and engineering department")
                checkdetails=int(input("press 1 to know about the course:"))
                if checkdetails==4:
                    print("this course about the computer hardwares and software and networking concepts")
                else:
                    print("enter the mentioned number")
                    #fees details
                semfees=int(input("press 1 to know semfees details:"))
                if semfees:
                    print(f"70000 per semester", "full fees>>",{70000*8} )
                else:
                    print("enter the correct option")
                busfees=int(input("press 2 to know bus fees details:"))
                if busfees:
                    print("15000 per semester")
                else:
                    print("enter the correct number")
                    
                admission=int(input("press 1 to admission:"))
                if admission:
                    print("your application is submitted")
                else:
                    print("please press 1")
    try:
        choice=int(input("choose which dept u want????:"))
        if choice==1:
            cse()
            back()
        if choice==2:
            eee()
            back()
        if choice==3:
            ece()
        if choice==4:
             mech()
    except:
        print("enter the correct option")
main()
            

        


