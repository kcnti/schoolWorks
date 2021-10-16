import mysql.connector
from mysql.connector import errorcode
import sys
name = sys.argv[1]

def query(data):
    try:
        cnx = mysql.connector.connect(user='root', host='localhost', database='student')
        cursor = cnx.cursor(buffered=True)
        _cursor = cnx.cursor()
        query = ("SELECT firstName, lastName, house_number, moo, street, soi,"
            "alley, amphur, postcode, age, weight, height, mobile, email,"
            "lineid, name_father, name_mother FROM student_m2_m5_63 WHERE identitySchoolNumber='" + data +"'")

        #fname = "Kantinun"
        #print("query done")
        cursor.execute(query)
        for _fname, _lname, house_number, moo, street, soi, alley, amphur, postcode, age, weight, height, mobile, email, lineid, name_father, name_mother in cursor:
            print(f"fname: {_fname}\nlname: {_lname}\nhouse number: {house_number}\nmoo: {moo}\nstreet: {street}\nsoi: {soi}\nalley: {alley}\namphur: {amphur}\npostcode: {postcode}\nage: {age}\nweight: {weight}\nheight: {height}\nmobile: {mobile}\nemail: {email}\nlineid: {lineid}\nfather: {name_father}\nmother: {name_mother}")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("user or password wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB not exist")
        else:
            print(err)
    else:
        cnx.close()
query(name)