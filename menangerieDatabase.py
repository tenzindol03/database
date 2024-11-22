import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rottenpotato03",
        database="menagerie"
    )

    mycursor = mydb.cursor()

    sql = "DROP DATABASE IF EXISTS menagerie"

    mycursor.execute(sql)
    print("Database 'menagerie' has been dropped (if it existed).")

except mysql.connector.Error as e:
    print(f"Error: {e}")
