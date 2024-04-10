import os
import sys
import mysql.connector as sql
sys.path.append(os.path.abspath('.'))
# module to connect to the database

def databaseConnect():

    cnx = sql.connect(host="localhost", user="root", password="hetu123456", database="hospital")
    print(cnx)
    return cnx

def search(table, column, value, constrain = "*"):

    cnx = databaseConnect()
    cursor = cnx.cursor()

    statement ="SELECT {0} FROM {1} WHERE {2} LIKE '%{3}%';".format(str(constrain), table, column, str(value))
    cursor.execute(statement)
    result = cursor.fetchall()
    for i in range(len(result)):
        print("ok")
        print(result[i])
    return result
#a multi use module enabling view, add, edit and delete data in sql

def get_input_fields(table):
    columns = {}
    cnx = databaseConnect()
    cursor = cnx.cursor(buffered=True)
    statement = "select * from {0};".format(table)
    cursor.execute(statement)
    content = cursor.description

    return content

def add(table, column_name4, column_value3):

    column = str(column_name4)
    column_name2 = column.replace("[", "")
    column_name3 = column_name2.replace("]", "")
    column_name = column_name3.replace("'", "`")

    column_value1 = str(column_value3)
    column_value2 = column_value1.replace("[", "")
    column_value = column_value2.replace("]", "")

    cnx = databaseConnect()
    cursor = cnx.cursor()
    statement2 = "INSERT INTO `hospital`.`{0}` ({1}) VALUES ({2});".format(str(table), column_name, column_value)
    print(statement2)
    cursor.execute(statement2)
    cnx.commit()
    cnx.close()

def edit(table, columns, values):
    cnx = databaseConnect()
    cursor = cnx.cursor()
    content = get_input_fields("{}".format(table))
    for i in range(len(columns)):
        variable = "{0}".format(content[i][0])

        if variable == "updatetime":
            break

        else:

            statement = "UPDATE `hospital`.`{0}` SET `{1}`='{2}' WHERE (`{3}` = '{4}');".format(
                    table, columns[i], values[i], columns[0], values[0])
            print(statement)
            cursor.execute(statement)


    cnx.commit()
    cnx.close()

def delete(table, primary_key_column, primary_key_value):
    cnx = databaseConnect()
    cursor = cnx.cursor()
    statement = "DELETE FROM `hospital`.`{0}` WHERE (`{1}` = '{2}');".format(table, str(primary_key_column),
                                                                             str(primary_key_value))
    print("Entry deleted")

    cursor.execute(statement)
    cnx.commit()
    cnx.close()