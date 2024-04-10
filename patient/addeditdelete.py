import mysql.connector as sql


def addeditdelete(mode, table):

    columns = {}
    cnx = sql.connect(host="localhost", user="root", password="hetu123456", database="hospital")
    print(cnx)
    cursor = cnx.cursor(buffered=True)
    statement = "select * from {}".format(table)
    cursor.execute(statement)
    content = cursor.description

    welcome = "Welcome to the {0} module. Add, edit or delete {0} records here.".format(table)
    print(welcome)
    if mode == 1:
        column_name = []
        column_value = []
        for i in range(len(content)):
            variable = "{0}".format(content[i][0])
            if variable == "updatetime":
                print('yes')
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
