import os
import sys
import patient.core_functions as cf
sys.path.append(os.path.abspath('.'))

def addeditdelete(mode, table):

    columns = {}
    cnx = cf.databaseConnect()
    cursor = cnx.cursor(buffered=True)
    content = cf.get_input_fields("{}".format(table))

    if mode == 0:

        column = input("What do you want to search? : ")


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

        cf.add("{}".format(table), column_name, column_value)
    elif mode == 2:

        column_names = []
        column_values = []

        print("Editing :")

        for i in range(len(content)):
            variable = "{0}".format(content[i][0])

            if variable == "updatetime":
                break

            else:
                statement1 = "Enter {}".format(variable)
                columns[variable] = input(statement1 + ": ")

            column_names.append(content[i][0])
            column_values.append(columns[content[i][0]])
        cf.edit(table, column_names, column_values)

        cnx.commit()
        cnx.close()

    elif mode == 3:

        statement1 = "Enter the {0} you want to delete: ".format(content[0][0])
        selected_record = int(input(statement1))

        column = content[0][0] #first field, is primary by design of db
        value = selected_record


        cf.delete(table,column,value)

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

            elif selection2 == 4:
                pass

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
