import mysql.connector as sql

# module to connect to the database

def databaseConnect():

    cnx = sql.connect(host="localhost", user="root", password="hetu123456", database="hospital")
    print(cnx)
    return cnx

#a multi use module enabling view, add, edit and delete data in sql
def addeditdelete(mode, table):

    columns = {}
    cnx = databaseConnect()
    cursor = cnx.cursor(buffered=True)
    statement = "select * from {0};".format(table)
    cursor.execute(statement)
    content = cursor.description

    if mode == 0:

        statement = "select * from hospital.{}".format(table)
        cursor.execute(statement)
        content = cursor.description

        rows = cursor.fetchall()
        print("Number of records: " + str(len(rows)))
        for i in rows:
            print(i)

    elif mode == 1:

        column_name = []
        column_value = []

        for i in range(len(content)):

            variable = "{0}".format(content[i][0])

            if variable == "updatetime":
                break

            else:
                statement1 = "Enter {}".format(variable)
                columns[variable] = input(statement1 + ": ")

                column_name1 = list(columns.keys())
                column_name.append(column_name1[i])
                column_value.append(columns[content[i][0]])

        column_name1 = str(column_name)
        column_name2 = column_name1.replace("[", "")
        column_name3 = column_name2.replace("]", "")
        column_name4 = column_name3.replace("'", "`")
        print(column_name4)

        column_value1 = str(column_value)
        column_value2 = column_value1.replace("[", "")
        column_value3 = column_value2.replace("]", "")
        print(column_value3)

        statement2 = "INSERT INTO `hospital`.`{0}` ({1}) VALUES ({2});".format(str(table), column_name4, column_value3)
        print(statement2)
        cursor.execute(statement2)
        cnx.commit()
        cnx.close()

    elif mode == 2:

        print("Editing :")

        for i in range(len(content)):
            variable = "{0}".format(content[i][0])

            if variable == "updatetime":
                break

            else:
                statement1 = "Enter {}".format(variable)
                columns[variable] = input(statement1 + ": ")

            statement = "UPDATE `hospital`.`{0}` SET `{1}`='{2}' WHERE (`{3}` = '{4}');".format(
                table, content[i][0], columns[content[i][0]], content[0][0], columns[content[0][0]])
            print(statement)

            cursor.execute(statement)

        cnx.commit()
        cnx.close()

    elif mode == 3:

        statement1 = "Enter the {0} you want to delete: ".format(content[0][0])
        selected_record = int(input(statement1))

        statement = "DELETE FROM `hospital`.`{0}` WHERE (`{1}` = '{2}');".format(table, content[0][0],
                                                                                 str(selected_record))

        cursor.execute(statement)

        print("The record is deleted!")

        cnx.commit()
        cnx.close()

#passes addeditdelete module parameters
def patient_functions():

    print("Welcome to the Patient module. Add, edit or delete patient records here.")

    while True:
        selection = int(input("What would you like to do?\n1.Add\n2.Edit\n3.Delete\n4.View Records\n5.Main Menu\n"))

        if selection == 1:
            addeditdelete(1, "patients")

        elif selection == 2:
            addeditdelete(2, "patients")

        elif selection == 3:
            addeditdelete(3, "patients")

        elif selection == 4:
            addeditdelete(0, "patients")

        elif selection == 5:
            break

#passes addeditdelete module parameters
def doctor_functions():

    print("Welcome to the Doctor module. Add, edit or delete doctor records here.")

    while True:
        selection = int(input("What would you like to do?\n1.Add\n2.Edit\n3.Delete\n4.View Records\n5.Main Menu"))

        if selection == 1:

            addeditdelete(1, "doctors")

        elif selection == 2:
            addeditdelete(2, "doctors")

        elif selection == 3:
            addeditdelete(3, "doctors")

        elif selection == 4:
            addeditdelete(0, "doctors")

        elif selection == 5:
            break

#passes addeditdelete module parameters
def inventory_functions():

    print("Welcome to the Inventory module. Add, edit or delete product records here.")
    selection1 = int(input("What would you like to do?\n1.Products\n2.Suppliers\n3.Main Menu"))

    while True:

        if selection1 == 1:
            selection2 = int(input("What would you like to do?\n1.Add\n2.Edit\n3.Delete\n4.Search\n5.View Records\n"
                                   "6.Prev Menu"))

            if selection2 == 1:
                addeditdelete(1, "inventory")

            elif selection2 == 2:
                addeditdelete(2, "inventory")

            elif selection2 == 3:
                addeditdelete(3, "inventory")

            elif selection2 == 5:
                addeditdelete(0, "inventory")

            elif selection2 == 6:
                break

        if selection1 == 2:

            selection2 = int(input("What would you like to do?\n1.Add\n2.Edit\n3.Delete\n4.Search\n5.View Records\n"
                                   "6.Prev Menu"))
            if selection2 == 1:

                addeditdelete(1, "supplier")

            elif selection2 == 2:

                addeditdelete(2, "supplier")

            elif selection2 == 3:
                addeditdelete(3, "supplier")

            elif selection2 == 5:
                addeditdelete(0, "supplier")

            elif selection2 == 6:
                break

#passes addeditdelete module parameters
def billing_functions():

    while True:
        selection2 = int(input("What would you like to do?\n1.Add\n2.Edit\n3.Search\n4.View Records\n5.Prev Menu"))
        if selection2 == 1:

            addeditdelete(1, "billing")

        elif selection2 == 2:

            addeditdelete(2, "billing")

        elif selection2 == 4:
            addeditdelete(0, "billing")

        elif selection2 == 5:
            break


def appoinments_functions():
    while True:
        selection2 = int(input("What would you like to do?\n1.Create\n2.Edit\n3.Search\n4.View Records\n5.Delete\n"
                               "6.Prev Menu"))
        if selection2 == 1:

            addeditdelete(1, "appoinments")

        elif selection2 == 2:

            addeditdelete(2, "appoinments")

        elif selection2 == 4:
            addeditdelete(0, "appoinments")

        elif selection2 == 5:
            addeditdelete(3, "appoinments")

        elif selection2 == 6:
            break
