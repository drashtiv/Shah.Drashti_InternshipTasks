import mysql.connector 
host_name = "localhost"
user_name = "root"
password = "root123"

my_con = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password
        )

mysqldb= mysql.connector.connect(host="localhost", user="root", passwd="root123", database="dbpython")
mycursor= mysqldb.cursor()
mycursor.execute("create table  if not exists studentData(enrollment_no int, name VARCHAR(50), marks INT)")

#while True:
user_input=int(input(" 1. Insert Data in the database \n 2. Display Data in the database \n 3. Update Data in the database \n 4. Delete Data in the database \n  "))

#Insert
if user_input==1:
    enrollment_no=int(input("Enter student enrollmet no. :"))
    name=input("Enter student name:")
    marks=int(input("Enter marks of the student :"))
    mycursor.execute("insert into studentData values({},'{}',{})".format(enrollment_no, name, marks))
    mysqldb.commit()
    
#Display
elif user_input==2:
    mycursor.execute("select * from studentData")
    result=mycursor.fetchall() 
    for i in result:    
      enrollment_no=i[0]  
      name=i[1]  
      marks=i[2]  
      print(enrollment_no,name,marks)

#Update
elif user_input==3:
    u_enrollmentNo=int(input("Enter the enrollment number"))
    new_name=input("Enter the updated name :")
    new_marks=input("Enter the updated marks :")
    mycursor.execute("UPDATE studentData SET name='{}', marks={} WHERE enrollment_no={}".format(new_name,new_marks,u_enrollmentNo))
    mysqldb.commit() 
    print('Record updated successfully...')
    
       
#Delete
elif user_input==4:
    roll_no=input("Enter the enrollment number of the student whose data you want to delete :")
    mycursor.execute("DELETE FROM studentData WHERE enrollment_no={}".format(roll_no))   
    mysqldb.commit() 
    print('Record deteted successfully...')

else:
    print("YOUR INPUT IS WRONG . PLEASE CHECK AGAIN")
mysqldb.close()