# sameple programme for python
import mysql.connector

connector = mysql.connector.connect(host="13.127.88.192",database="itps_db", user="itps_db_user", passwd="IjRJnKj2hFknimX7vkUc")

mycursor = connector.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)