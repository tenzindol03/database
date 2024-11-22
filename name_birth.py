import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rottenpotato03",
    database="menagerie"
)

cursor = mydb.cursor()

cursor.execute("SELECT name, birth FROM pet;")

print(f"{'Name':<10} {'Birth Date':<12}")
print("-" * 25)

for name, birth in cursor:
    print(f"{name:<10} {birth}")

cursor.close()
mydb.close()
