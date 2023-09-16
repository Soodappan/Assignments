

def chennai():
    print ("""CHENNAI=>1. Kapaleeshwarar Temple
    2. VGP Snow Kingdom
    3. San Thome Church
    4. Besant Nagar Beach
    5. Marina Beach""")

    choose = input('enter the type of travel AC/NON AC:')
    if choose == 'ac':
        print ('for ac coach 2000 per head')
    elif choose == 'non ac':
        print ('for non ac coach 1500 per head')
    else:
        print (' enter the correct number')
    again = input('do u want to go back press YES:')
    if again == 'yes':
        main()
    else:
        print (' welcome')
def madurai():
    print (""" MADURAI=>1. Madurai Meenakshi Amman Temple
    2. Aayiram Kaal Mandapam
    3. Pazhamudhir Solai
    4. Alagarkoil Temple and Shrine
    5. Gandhi Memorial """)

    choose = input('enter the type of travel AC/NON AC:')
    if choose == 'ac':
         print ('for ac coach 3000 per head')
    elif choose == 'non ac':
        print ('for non ac coach 2500 per head')
    else:
         print (' enter the correct number')
    again = input('do u want to go back press YES:')
    if again == 'yes':
        main()
    else:
        print (' welcome')

def covai():
    print ("""COVAI=>1. Adiyogi Shiva
    2. Dhyanalinga Temple
    3. Arulmigu Patteeswarar Swamy Temple
    4. Marudamalai Temple
    5. Marudhamalai """)

    choose = input('enter the type of travel AC/NON AC:')
    if choose == 'ac':
        print ('for ac coach 4000 per head')
    elif choose == 'non ac':
        print ('for non ac coach 3500 per head')
    else:
        print (' enter the correct number')
    again = input('do u want to go back press YES:')
    if again == 'yes':
        main()
    else:
        print (' welcome')

def kumari():
    print ("""Thirparappu Falls, 
    Vivekananda Rock Memorial, 
    Thanumalayan Temple - 
    Sthanumalayan Kovil, 
    Thiruvalluvar""")

    choose = input('enter the type of travel AC/NON AC:')
    if choose == 'ac':
        print ('for ac coach 5000 per head')
    elif choose == 'non ac':
        print ('for non ac coach 4500 per head')
    else:
        print (' enter the correct number')
    again = input('do u want to go back press YES:')
    if again == 'yes':
        main()
    else:
        print (' welcome')

def banglore():
    print ('''1. Bannerghatta National Park \xc2\xb7 
    2. Chunchi Falls \xc2\xb7 
    3. Ulsoor Lake \xc2\xb7 
    4. Bangalore Aquarium.''')

    choose = input('enter the type of travel AC/NON AC:')
    if choose == 'ac':
        print ('for ac coach 6000 per head')
    elif choose == 'non ac':
         print ('for non ac coach 5500 per head')
    else:
        print (' enter the correct number')
    again = input('do u want to go back press YES:')
    if again == 'yes':
        main()
    else:
         print (' welcome')
def main():
    print ('***WELCOME TO PKS TRAVELS***')
    print ('press(1)to book CHENNAI')
    print ('press(2)to book MADURAI')
    print ('press(3)to book COVAI')
    print ('press(4)to book KUMARI')
    print ('press(5)to book BANGLORE')
    x= int(input(" Enter any number:"))
    
    if x==1:
        chennai()
    elif x==2:
        madurai()
    elif x==3:
        covai()
    elif x==4:
        kumari()
    elif x==5:
        banglore()
    else:
        print ('press only available keys')
main()