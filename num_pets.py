import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rottenpotato03",
    database="menagerie"
)

cursor = mydb.cursor()

cursor.execute("""
    SELECT owner, COUNT(*) AS pet_count
    FROM pet
    GROUP BY owner;
""")

print(f"{'Owner':<10} {'Number of Pets':<15}")
print("-" * 25)

for owner, pet_count in cursor:
    print(f"{owner:<10} {pet_count:<15}")

cursor.close()
mydb.close()
