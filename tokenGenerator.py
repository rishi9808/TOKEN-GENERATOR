from optparse import Values
import mysql.connector as myconn
c=myconn.connect(host='localhost',password='root',user='root',database='HOSPITAL')
if (c.is_connected()):
    pass
    print("connected")
cur=c.cursor()
name=""
phone=""

print("\n <---- TOKEN GENERATOR -->\n")

print("-- CLIENT SIDE --\n")

def patientDetail():
    name=input("enter patient name : ")
    phone=input("enter phone num: ")
    age=int(input("enter age: "))
    doc_name=input("enter doctor name: ")
    print(" ")
    #insert Values
    q1="insert into patientDetail(name,phone,age,Doctor) values('{}','{}',{},'{}')".format(name,phone,age,doc_name)
    cur.execute(q1)
    c.commit()

    #show token value
    cur.execute("Select token from patientDetail where name='{}'".format(name))
    token=cur.fetchall()
    for i in token:
        print("TOKEN GENERATED \n")
        print("YOUR TOKEN NUMBER IS:",i[0])


    print("\n-- SERVER SIDE --\n")
    sqlDisplay()

def sqlDisplay():
    print('..........PATIENT DETAILS..........')
    print('')
    print('token  name  phone  age  Doctor')
    cur.execute('Select * from patientDetail')
    a=cur.fetchall()
    for i in a:
        print(i[0],' ',i[1],' ',i[2],' ',i[3],' ',i[4])
    print('---------------------------------------------------------')
patientDetail()





