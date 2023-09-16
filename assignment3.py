print(" welcome to banigar pg")
print("""select the sharing option
    1.one share
    2.two share
    3.three share
    4.four sharing
    5.five sharing  """)
# input
option=(int(input("select  the option you want:")))
#value 
o=8000
t=7500
th=6500
f=6000
fi=5500
ad=2000
 # function call
def one(o,ad):
   return o+ad
def two(t,ad):
   return t+ad
def three(th,ad):
   return th+ad
def four(f,ad):
   return f+ad
def five(fi,ad):
   return fi+ad
# function call
if   option==1:
  print("your rent is:",one(o,ad))
if option==2:
  print("your rent is:",two(t,ad))
if option==3:
  print("your rent is:",three(th,ad))
if option==4:
  print("your rent is",four(f,ad))
if option==5:
  print("your rent is:",five(fi,ad))
else:
  ("print select the another option")
