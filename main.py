import os
import sys

import patient.functions as pf
import patient.core_functions as cf
print(sys.version)
cnx = cf.databaseConnect() #module to connect database
cursor = cnx.cursor()
print("Welcome to Health DBMS.")

auth = 0
priviledge = 0
user = input("Enter your user_ID: ")
passwd = input("Enter your password: ")

statement1 = "select * from users;"
cursor.execute(statement1)
allowedUsers = cursor.fetchall()



for i in range(len(allowedUsers)):
    if user == allowedUsers[i][0] and passwd == allowedUsers[i][1]:
        print("Successfully logged in\n")
        auth = 1
        priviledge = int(allowedUsers[i][2])

        break
    else:
        print("User_ID and password do not match.")
        break

print(auth)
print(priviledge)

if auth == 1:
    if priviledge == 1:
        while True:
            module_selection = int(input("Select a module: \n1.Patients\n2.Doctors\n3.Inventory\n4.Billing\n5.Messages\n6.Appoinments\n7.Exit\n"))
            if module_selection == 1:
                pf.patient_functions()
            elif module_selection == 2:
                pf.doctor_functions()
            elif module_selection == 3:
                pf.inventory_functions()
            elif module_selection == 4:
                pf.billing_functions()
            elif module_selection == 6:
                pf.appoinments_functions()
            elif module_selection == 7:
                break

else:
    print("Unauthorized!")

