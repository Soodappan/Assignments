def add_data():
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="testing"
    )
    #connect the database
    mycursor=mydb.cursor()
    #insert data into the table
    newdata="insert into students(id,name,dept,year,fees)value(%s,%s,%s,%s,%s)"
    print("*******register*********")
    id=int(input("enter your three digits id:"))
    name=(input("enter your name:"))
    dept=(input("enter your dept:"))
    year=(input("enter your year:"))
    fees=int(input("enter your fees:"))
    value=(id,name,dept,year,fees)
    mycursor.execute(newdata,value)
    mydb.commit()
    print("your data has been inserted")
    again=int(input("do u want to goto first page press 1:"))
    if again==1:
        add_data()
    else:
        print("thnk u")    

add_data()


